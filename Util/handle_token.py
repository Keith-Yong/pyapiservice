import os
from Util.handle_json import read_json, write_value

"""获取token 写入token 携带token"""


def get_token_value(token_key):
    """获取token"""
    data = read_json("token.json")  # 调用read_json获取token
    return data[token_key]


def write_token(data, token_key):
    """写入token到token.json文件中"""
    data1 = read_json("token.json")  # 读取后更新token的value
    data1[token_key] = data
    write_value(data1)  # 写入


if __name__ == '__main__':
    data = {
        "Authorization": "22"
    }

    print(write_token(data, "web"))
