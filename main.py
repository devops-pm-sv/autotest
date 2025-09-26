# encoding: utf-8
# @Time    : 2020/12/1 13:59
# @Author  : zhoubo
# @dsc     :
import unittest
import sys
import time
from autotest.report.BeautifulReport import BeautifulReport

class Assert(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.case_result = False

    @classmethod
    def set_pass(self, msg='') -> None:
        sys.stdout.write(msg)

    @classmethod
    def set_fail(self, msg="测试失败!") -> None:
        raise Assert.failureException(msg)


if __name__ == '__main__':
    # ts = unittest.TestSuite()
    # ts.addTest(unittest.makeSuite(Test))
    # filename = "123" + '.html'
    # # 加载执行用例生成报告
    # result = BeautifulReport(ts)
    # # 定义报告属性
    # filepath = "E:\PyProject\\autotest\log"
    # result.report(description='XXX报告XX描述', filename=filename, log_path=filepath)

    test_dir = "E:\PyProject\\autotest\\testsuit"
    report_dir = "E:\PyProject\\autotest\\report"
    discover = unittest.defaultTestLoader.discover(test_dir, 'test*.py', None)
    filename = '测试报告'
    # unittest.TextTestRunner
    BeautifulReport(discover).report(description='测试', filename=filename, log_path=report_dir)




































