import json
import os
from Util.handle_excel import excel_data

from jsonpath_rw import parse

base_path = os.path.abspath(os.path.dirname(os.getcwd()))


def split_data(data):
    """拆分依赖数据"""

    case_id = data.split(">")[0]
    rule_key = data.split(">")[1]

    return case_id, rule_key


def depend_data(data):
    """获取依赖结果集"""
    case_id = split_data(data)[0]

    columns = excel_data.get_columns_value()

    for column_data in columns:
        """根据case的名称获取case的行号，结果集"""
        if case_id == column_data:
            row_num = excel_data.get_rows_number(case_id)
            res_data = excel_data.get_cell_value(row_num, 14)
            return res_data


def get_depend_value(res, rule_key):
    """解析依赖规则并获取依赖值"""

    res = json.loads(res)

    json_exe = parse(rule_key)
    madle = json_exe.find(res)
    return [math.value for math in madle][0]


def get_data(data):
    """调用并获取最终依赖值"""
    res_data = depend_data(data)
    rule_key = split_data(data)[1]

    depend_value = get_depend_value(res_data, rule_key)

    return depend_value


if __name__ == '__main__':
    data = '{"data":{"id": "1"}}'
    key = '$..id'
    print(get_depend_value(data, key))
