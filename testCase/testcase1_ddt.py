import os
import ddt
import unittest
import json
from Util.handle_excel import excel_data
from Common.baserequest import BaseRequest
from Util.handle_result import handle_result_msg, handle_result_json, get_result_json
from Util.handle_token import get_token_value
from Util.handle_condition import get_data
# import jsonpath
from Common.mockvalue import mock_depend

base_path = os.path.abspath(os.path.dirname(os.getcwd()))
data = excel_data.get_excel_data()


@ddt.ddt
class Test_Index(unittest.TestCase):
    """执行case主流程"""

    @classmethod
    def setUpClass(cls):
        print('测试环境准备')

    @classmethod
    def tearDownClass(cls):
        print('测试环境清理')

    @ddt.data(*data)
    def test_mainindex(self, data):
        """执行case主流程"""

        case_id = data[0]
        i = excel_data.get_rows_number(case_id)  # 行号

        header = None
        get_token = None

        is_run = data[2]

        if is_run == "yes":

            data1 = json.loads(data[7])
            is_depend = data[3]
            try:
                if is_depend:
                    """获取依赖数据"""
                    depend_key = data[4]
                    try:
                        depend_value = get_data(is_depend)
                    except:  # 依赖接口失败启动 mock函数获取依赖数据
                        depend_value = mock_depend()  # mock依赖
                    data1[depend_key] = depend_value

                url = data[5]
                method = data[6]

                expected_method = data[10]

                token_method = data[9]
                if token_method == 'yes':
                    """携带token"""
                    data2 = get_token_value("web")

                    header = data2
                if token_method == "write":
                    """写入token"""
                    get_token = {"is_token": "web"}

                res = BaseRequest.run(method, url, data1, get_token, header)

                code = res['meta']["status"]
                message = res['meta']["msg"]

                if expected_method == "mec":
                    configmes = handle_result_msg(url, code)

                    try:
                        self.assertEqual(configmes, message)
                        excel_data.excel_write_data(i, 13, "通过")
                    except AssertionError as e:
                        excel_data.excel_write_data(i, 13, "失败", "red")
                        raise e

                if expected_method == "json":  # expected_method自定义校验方法
                    if code == 200 or code == 201:
                        status_str = "success"

                    else:
                        status_str = "error"

                    except_res = get_result_json(url, status_str)
                    result = handle_result_json(res, except_res)

                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(i, 13, "通过")
                    except AssertionError as e:
                        excel_data.excel_write_data(i, 13, "失败", "red")
                        raise e
            except Exception as e:
                raise e
            finally:
                excel_data.excel_write_data(i, 14, json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    unittest.main()
