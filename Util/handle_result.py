import os
from deepdiff import DeepDiff

base_path = os.path.abspath(os.path.dirname(os.getcwd()))

from Util.handle_json import get_value


def handle_result_msg(url, code):
    """断言方式为mec时调用此函数获取对应的信息"""
    data = get_value(url, "code_message.json")
    if data is not None:
        for i in data:
            message = i.get(str(code))  # 这里需要把参数code转行为str类型
            if message:
                return message
    return None


def get_result_json(url, status):
    """断言方式为json时获取对应的Json数据"""
    data = get_value(url, "result.json")

    if data is not None:
        for i in data:
            message = i.get(status)  # 这里需要把参数code转行为str类型
            if message:
                return message


def handle_result_json(dict1, dict2):
    """复杂json返回值处理"""

    if isinstance(dict1, dict) and isinstance(dict2, dict):
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()

        if not (cmp_dict.get("dictionary_item_added") or cmp_dict.get("dictionary_item_removed")):
            return True
        else:
            return False
    return False


if __name__ == '__main__':
    print()
