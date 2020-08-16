import os
import requests
from Util.handle_ini import HadnleIni
import json
from Util.handle_json import get_value
from Util.handle_token import write_token
import jsonpath

base_path = os.path.abspath(os.path.dirname(os.getcwd()))
request = requests.Session()


class BaseRE():
    """基础请求"""

    def send_post(self, url, data, get_token=None, header=None):
        """post请求"""
        res = request.post(url=url, data=data, headers=header).json()
        if get_token is not None:
            """token写入"""
            token = ' '.join(jsonpath.jsonpath(res, '$..token'))

            header2 = {"Authorization": token}
            write_token(header2, get_token["is_token"])

        return res

    def send_get(self, url, data, get_token=None, header=None):
        """get请求"""

        if len(data) == 1:
            """路径get"""
            para = "/"
            for key, value in data.items():
                if len(data) == 1:
                    para += str(value)
            url = url + para
            res = request.get(url=url, headers=header).json()

        res = request.get(url=url, params=data, headers=header).json()
        if get_token is not None:
            # token写入
            token_rule = HadnleIni.get_value("token_rule", json)
            token = jsonpath.jsonpath(res, token_rule)[0]
            header2 = {"Authorization": token}
            write_token(header2, get_token["is_token"])

        return res

    def run(self, method, url, data=None, get_token=None, header=None):
        """请求主函数run(method, url, data1, cookie,get_token, header=header"""

        base_url = HadnleIni.get_value("host")

        if "http" not in url and "https" not in url:  # url构建
            url = base_url + url

        if method == "post":
            res = self.send_post(url, data, get_token, header)
        elif method == "get":
            res = self.send_get(url, data, get_token, header)

        return res


BaseRequest = BaseRE()
if __name__ == '__main__':
    BaseRequest = BaseRE()
