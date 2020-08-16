import os
import json

base_path = os.path.abspath(os.path.dirname(os.getcwd()))


def read_json(file_name=None):
    """读取Json文件中的所有数据"""

    if file_name is None:
        """默认读取user_data.json"""
        file_path = os.path.join(base_path, "Config", "user_data.json")

    else:
        file_path = os.path.join(base_path, "Config", file_name)

    with open(file_path, encoding='UTF-8') as f:
        data = json.load(f)  # 用于从json文件中读取数据

    return data


def get_value(key, file_name=None):
    """获取具体的json字符串"""
    data = read_json(file_name)
    return data.get(key)  # 这里使用get否则报错


def write_value(data, file_name=None):
    """把数据写入文件中"""
    if isinstance(data, dict):
        data = json.dumps(data)  # 转化成json才能写入Json文件
    if file_name is None:  # 默认写入token.json文件中
        file_path = os.path.join(base_path, "Config", "token.json")
    else:  # 根据文件名称写入对应的文件中
        file_path = os.path.join(base_path, "Config", file_name)
    with open(file_path, "w") as f:
        f.write(data)


if __name__ == '__main__':
    print()
