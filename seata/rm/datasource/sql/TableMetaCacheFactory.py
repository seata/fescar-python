#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.context.RootContext import RootContext
from seata.exception.NotSupportYetException import NotSupportYetException
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.Types import Types
from seata.rm.datasource.sql.struct.ColumnMeta import ColumnMeta
from seata.rm.datasource.sql.struct.IndexMeta import IndexMeta
from seata.rm.datasource.sql.struct.IndexType import IndexType
from seata.rm.datasource.sql.struct.TableMeta import TableMeta
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class TableMetaCacheFactory:

    @classmethod
    def get_table_meta_cache(cls, db_type: str):
        if db_type != JdbcConstants.MYSQL:
            raise NotSupportYetException("not support " + db_type)
        return MySQLTableMetaCache()


class TableMetaCache:
    CACHE = {}

    def get_table_meta(self, connection, table_name, resource_id):
        if table_name is None or table_name.strip() == '':
            raise ValueError("table name is blank")
        cache_key = self.get_cache_key(connection, table_name, resource_id)
        table_meta = self.CACHE.get(cache_key, None)
        if table_meta is None:
            try:
                table_meta = self.fetch_schema(connection, table_name)
                self.CACHE[cache_key] = table_meta
            except Exception as e:
                print('get table meta error.', e)
        if table_meta is None:
            raise ShouldNeverHappenException('xid:{}, get table meta error. check {} table whether exists.'.format(
                RootContext.get_xid(), table_meta))
        return table_meta

    def refresh(self, connection, resource_id):
        cache = self.CACHE
        for k, v in cache:
            key = self.get_cache_key(connection, v.table_name, resource_id)
            if k == key:
                try:
                    table_meta = self.fetch_schema(connection, v.table_name)
                    if table_meta != v:
                        self.CACHE[k] = table_meta
                        print('table meta change was found. key:' + key)
                except Exception as e:
                    print('table meta refresh error', e)

    def get_cache_key(self, connection, table_name, resource_id):
        pass

    def fetch_schema(self, connection, table_name):
        pass


class MySQLTableMetaCache(TableMetaCache):

    def get_cache_key(self, connection, table_name, resource_id):
        cache_key = resource_id + "."
        table_name_with_schema = table_name.replace("`", "").split(".")
        if len(table_name_with_schema) > 1:
            default_table_name = table_name_with_schema[1]
        else:
            default_table_name = table_name_with_schema[0]
        try:
            cursor = connection.cursor()
            sql = "select * from information_schema.global_variables WHERE variable_name = 'LOWER_CASE_TABLE_NAMES'"
            cursor.execute(sql)
            one = cursor.fetchone()
            if one[1] == '1':
                cache_key += default_table_name
            else:
                cache_key += default_table_name.lower()
            return cache_key
        except Exception as e:
            print('fetch global variables error', e)
            cache_key += default_table_name
            return cache_key

    def fetch_schema(self, connection, table_name):
        cursor = connection.cursor()
        schema = connection._pool._kwargs['database']
        columns_sql = "select * from information_schema.columns where table_name = %s and table_schema = %s"
        cursor.execute(columns_sql, (table_name, schema))
        columns_all = cursor.fetchall()
        table_meta = TableMeta()
        table_meta.table_name = table_name
        for i in range(len(columns_all)):
            r = columns_all[i]
            col = ColumnMeta()
            col.table_cat = r[0]  # TABLE_CATALOG
            col.table_schema_name = r[1]  # TABLE_SCHEMA
            col.table_name = r[2]  # TABLE_NAME
            col.column_name = r[3]  # COLUMN_NAME
            col.ordinal_position = r[4]  # ORDINAL_POSITION
            # col. = r[5] # COLUMN_DEFAULT
            col.is_nullable = r[6]  # IS_NULLABLE
            col.data_type_name = r[7]  # DATA_TYPE
            col.data_type = Types.get(col.data_type_name)
            # col. = r[8] # CHARACTER_MAXIMUM_LENGTH
            col.char_octet_length = r[9]  # character_octet_length
            col.num_prec_radix = r[10]  # NUMERIC_PRECISION
            # col. = r[11] # NUMERIC_SCALE
            # col. = r[12] # DATETIME_PRECISION
            # col. = r[13] # CHARACTER_SET_NAME
            # col. = r[14] # COLLATION_NAME
            # col. = r[15] # COLUMN_TYPE
            # col. = r[16] # COLUMN_KEY
            # r[17] # EXTRA
            if 'auto_increment' in r[17]:
                col.is_autoincrement = 'YES'
            else:
                col.is_autoincrement = 'NO'
            # col. = r[18] # PRIVILEGES
            # col. = r[19] # COLUMN_COMMENT
            # col. = r[20] # IS_GENERATED
            # col. = r[21] # GENERATION_EXPRESSION
            table_meta.all_columns[col.column_name] = col

        # indexs_sql = "select * from information_schema.statistics where table_schema = %s and table_name = %s"
        indexs_sql = "show index from {} from {}".format(table_name, schema)
        cursor.execute(indexs_sql)
        indexs_all = cursor.fetchall()
        for i in range(len(indexs_all)):
            r = indexs_all[i]
            table_name = r[0]  # Table
            non_unique = r[1] == 1  # Non_unique
            index_name = r[2]  # Key_name
            column_name = r[4]  # Column_name
            cardinality = r[6]  # Cardinality
            col = table_meta.all_columns[column_name]
            if table_meta.all_indexs.get(index_name, None) is not None:
                table_meta.all_indexs[index_name].values.append(col)
            else:
                im = IndexMeta()
                im.index_name = index_name
                im.non_unique = non_unique
                # im.index_qualifier =
                # im.type =
                # im.ordinal_position =
                # im.asc_or_desc =
                im.cardinality = cardinality
                if "PRIMARY" == index_name:
                    im.index_type = IndexType.PRIMARY
                elif not im.non_unique:
                    im.index_type = IndexType.UNIQUE
                else:
                    im.index_type = IndexType.NORMAL
                im.values.append(col)
                table_meta.all_indexs[index_name] = im
        if len(table_meta.all_indexs) == 0:
            raise ShouldNeverHappenException('not found any index int the table : ' + table_name)
        return table_meta
