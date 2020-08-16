import os
import unittest
import HTMLTestRunner
from Common.Log import logger

base_path = os.path.abspath(os.path.dirname(os.getcwd()))

report_path = os.path.join(base_path, 'Report')


class RunCase():
    """框架启动入口，写入日志，unittest入口"""

    def __init__(self):  # 重要信息写入日志
        report_paths = os.path.join(report_path, "report.html")
        self.caseFile = os.path.join(base_path, "testCase", "testcase1_ddt.py")

        logger.info('{}'.format(report_paths))
        logger.info('{}'.format(self.caseFile))

    def runcase(self):  # unittest discover管理case

        case_path = os.path.join(base_path, "testCase")

        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")

        result_path = os.path.join(base_path, "Report", "report.html")
        with open(result_path, "wb") as f:
            runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="测试报告", description="测试人员：ysz")
            runner.run(discover)


if __name__ == '__main__':
    RunCase = RunCase()
    RunCase.runcase()
