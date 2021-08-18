#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


class DataCompareUtil:
    @classmethod
    def is_records_equals(cls, before_image, after_image):
        if before_image is None:
            return (after_image is None, None, None)
        else:
            if after_image is None:
                return (False, None, None)
            if before_image.table_name.lower() == after_image.table_name.lower() and \
                            len(before_image.rows) == len(after_image.rows):
                if len(before_image.rows) == 0:
                    return (True, None, None)
                return cls.__compare_rows(before_image.table_meta, before_image.rows, after_image.rows)
            else:
                return (False, None, None)

    @classmethod
    def __compare_rows(cls, table_meta, old_rows, new_rows):
        old_rows_map = cls.__row_list_to_map(old_rows, table_meta.get_primary_key_only_name())
        new_rows_map = cls.__row_list_to_map(new_rows, table_meta.get_primary_key_only_name())

        for key, old_row in old_rows_map.items():
            new_row = new_rows_map[key]
            if new_row is None:
                return (False, 'compare row failed, rowKey {}, reason [newRow is null]', (key,))
            for field_name, old_field in old_row.items():
                new_field = new_row[field_name]
                if new_field is None:
                    return (
                        False, 'compare row failed, rowKey {}, fieldName {}, reason [newField is null]',
                        (key, field_name))
                old_equals_new_field_result = cls.__is_field_equals(old_field, new_field)
                if not old_equals_new_field_result[0]:
                    return old_equals_new_field_result
        return (True, None, None)

    @classmethod
    def __row_list_to_map(cls, row_list, primary_key_list):
        row_map = {}
        for i in range(len(row_list)):
            row = row_list[i]
            row_field_list = sorted(row.fields, key=lambda x: x.name)
            cols_map = {}
            row_key = ""
            first_under_line = False
            for j in range(len(row_field_list)):
                field = row_field_list[j]
                if field.name in primary_key_list:
                    if first_under_line and j > 0:
                        row_key += "_"
                    row_key += str(field.value)
                    first_under_line = True
                cols_map[field.name.strip().upper()] = field
            row_map[row_key] = cols_map
        return row_map

    @classmethod
    def __is_field_equals(self, old_field, new_field):
        if old_field is None:
            return (new_field is None, None, None)
        else:
            if new_field is None:
                return (False, None, None)
            else:
                if old_field.name.lower() == new_field.name.lower() and old_field.type == new_field.type:
                    if old_field.value is None:
                        return (new_field.value is None, None, None)
                    else:
                        if new_field.value is None:
                            return (False, "field not equals, name {}, new value is null", (old_field.name,))
                        else:
                            # TODO deep equals
                            result = old_field.value == new_field.value
                            if result:
                                return (True, None, None)
                            else:
                                return (False, "field not equals, name {}, old value {}, new value {}",
                                        (old_field.name, old_field.value, new_field.value))
                else:
                    return (False, "Field not equals, old name {} type {}, new name {} type {}", (old_field.name, old_field.type, new_field.name, new_field.type))
