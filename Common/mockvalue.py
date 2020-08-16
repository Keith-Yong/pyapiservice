import json

import mock
from Util.handle_condition import get_data


def mock_depend():
    """mock依赖数据"""
    data = {
        "data": {
            "cat_id": 1750,
            "cat_name": "橘子",
            "cat_level": "2",
            "cat_deleted": False
        },
        "meta": {
            "msg": "创建成功",
            "status": 201
        }
    }

    depend_value = data.get('data').get('cat_id')
    get_data = mock.Mock(return_value=depend_value)
    res = get_data

    return res()
