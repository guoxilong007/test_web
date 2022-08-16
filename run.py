import unittest
from common import getpath, HTMLTestRunnerNew

# 1、实例化一个loader对象和suite对象
loader = unittest.TestLoader()
suite = unittest.TestSuite()
# 2、使用discover去找到目录下所有的测试用例
suite.addTest(loader.discover(getpath.test_case_path))

web_testcase = open(getpath.report_path, "wb")
runner = HTMLTestRunnerNew.HTMLTestRunner(stream=web_testcase, title="boxuegu——test", description="单元测试报告",
                                          tester="GXL")
runner.run(suite)