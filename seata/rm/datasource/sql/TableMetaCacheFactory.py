#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from loguru import logger

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
                logger.error('get table meta error.', e)
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
                        logger.warning('table meta change was found. key:' + key)
                except Exception as e:
                    logger.error('table meta refresh error', e)

    def get_cache_key(self, connection, table_name, resource_id):
        raise NotImplemented('need subclass implemented')

    def fetch_schema(self, connection, table_name):
        raise NotImplemented('need subclass implemented')


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
            logger.error('fetch global variables error', e)
            cache_key += default_table_name
            return cache_key

    def fetch_schema(self, connection, table_name):
        cursor = connection.cursor()
        # the connection from connection_proxy has db_type, database
        schema = connection.database
        columns_sql = "select * from information_schema.columns where table_name = %s and table_schema = %s"
        cursor.execute(columns_sql, (table_name, schema))
        columns_all = cursor.fetchall()
        table_meta = TableMeta()
        table_meta.table_name = table_name

        col_description = cursor.description
        col_desc_map = {}
        for idx, d in enumerate(col_description):
            col_desc_map[d[0].upper()] = idx

        for i in range(len(columns_all)):
            rs = columns_all[i]
            col = ColumnMeta()
            col.table_cat = rs[col_desc_map['TABLE_CATALOG']]  # TABLE_CATALOG
            col.table_schema_name = rs[col_desc_map['TABLE_SCHEMA']]  # TABLE_SCHEMA
            col.table_name = rs[col_desc_map['TABLE_NAME']]  # TABLE_NAME
            col.column_name = rs[col_desc_map['COLUMN_NAME']]  # COLUMN_NAME
            col.ordinal_position = rs[col_desc_map['ORDINAL_POSITION']]  # ORDINAL_POSITION
            # col. = rs[desc_map['COLUMN_DEFAULT']] # COLUMN_DEFAULT
            col.is_nullable = rs[col_desc_map['IS_NULLABLE']]  # IS_NULLABLE
            col.data_type_name = rs[col_desc_map['DATA_TYPE']]  # DATA_TYPE
            col.data_type = Types.get(col.data_type_name.upper())
            # col. = r[desc_map['CHARACTER_MAXIMUM_LENGTH']] # CHARACTER_MAXIMUM_LENGTH
            col.char_octet_length = rs[col_desc_map['CHARACTER_OCTET_LENGTH']]  # CHARACTER_OCTET_LENGTH
            col.num_prec_radix = rs[col_desc_map['NUMERIC_PRECISION']]  # NUMERIC_PRECISION
            # col. = r[desc_map['NUMERIC_SCALE']] # NUMERIC_SCALE
            # col. = r[desc_map['DATETIME_PRECISION']] # DATETIME_PRECISION
            # col. = r[desc_map['CHARACTER_SET_NAME']] # CHARACTER_SET_NAME
            # col. = r[desc_map['COLLATION_NAME']] # COLLATION_NAME
            # col. = r[desc_map['COLUMN_TYPE']] # COLUMN_TYPE
            # col. = r[desc_map['COLUMN_KEY']] # COLUMN_KEY
            # EXTRA
            col_extra = rs[col_desc_map['EXTRA']]
            if 'auto_increment' in col_extra:
                col.is_autoincrement = 'YES'
            else:
                col.is_autoincrement = 'NO'
            # col. = r[desc_map['PRIVILEGES']] # PRIVILEGES
            # col. = r[desc_map['COLUMN_COMMENT']] # COLUMN_COMMENT
            # col. = r[] # IS_GENERATED
            # col. = r[] # GENERATION_EXPRESSION
            table_meta.all_columns[col.column_name] = col

        # indexs_sql = "select * from information_schema.statistics where table_schema = %s and table_name = %s"
        indexs_sql = "show index from {} from {}".format(table_name, schema)
        cursor.execute(indexs_sql)
        indexs_all = cursor.fetchall()

        idx_description = cursor.description
        idx_desc_map = {}
        for idx, d in enumerate(idx_description):
            idx_desc_map[d[0].upper()] = idx

        for i in range(len(indexs_all)):
            rs = indexs_all[i]
            table_name = rs[idx_desc_map['TABLE']]  # Table
            non_unique = rs[idx_desc_map['NON_UNIQUE']] == 1  # Non_unique
            index_name = rs[idx_desc_map['KEY_NAME']]  # Key_name
            column_name = rs[idx_desc_map['COLUMN_NAME']]  # Column_name
            cardinality = rs[idx_desc_map['CARDINALITY']]  # Cardinality
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
