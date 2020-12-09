# encoding: utf-8
# @Time    : 2020/12/4 11:53
# @Author  : zhoubo
# @dsc     :
import unittest
from autotest.report.BeautifulReport import BeautifulReport
import time
from autotest.main import Assert
from autotest.log.log import LogSet
import configparser
import os
from autotest.common.request_op import Other


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("这是setupclass")
        LogSet.debug(msg="这是setupclass")

    @classmethod
    def tearDownClass(cls) -> None:
        LogSet.debug(msg="这是teardownclass")


    def tesm(self):
        print(9999)


    def test1(self):
        '''# dfhdfghdgfh'''
        o  = Other()
        o.tt(m="498646",s="mmmmm")

        print(123)
        a = 123
        # self.assertEqual(1,2)
        self.fail(msg="这就失败了")


    # @unittest.skip("21")
    def test2(self):
        '''fghgfnnnghnfghngf56364636434'''
        o  = Other()
        o.tt("mmmmm","ssss")
        a = 1
        b = 2

    def test3(self):
        # time.sleep(50)
        '''gfhgggggggggggghngf'''
        o  = Other()
        o.tr()
        print(3333333)
        # Aeest.set_pass()



class Test2(unittest.TestCase):

    def setUp(self) -> None:
        print("这是setup")

    def tearDown(self) -> None:
        print("这是teardown")

    def tesm(self):
        print(9999)

    def test11(self):
        print(self.id(),"1+1")
        '''dfhdfghdgfh
        gjoyuliu'''
        print(123)
        time.sleep(2)
        a = 123



    # @unittest.skip("tiao tiao")
    def test22(self):
        '''fghgfnnnghnfghngf56364636434'''
        print(456)
        a = 1
        b = 2
        # Assert.set_fail(f"期望{a}实际{b}")

    def test33(self):
        # time.sleep(50)
        '''gfhgggggggggggghngf'''
        print(3333333)
        # Aeest.set_pass()

if __name__ == '__main__':
    pass
    ts = unittest.TestSuite()
    ts.addTest(unittest.makeSuite(Test))
    filename = "123" + '.html'
    # 加载执行用例生成报告
    result = BeautifulReport(ts)
    # 定义报告属性
    # filepath = "E:\PyProject\\autotest\log"
    # result.report(description='XXX报告XX描述', filename=filename, log_path=filepath)

    import os

    curPath = os.path.abspath(os.path.dirname(__file__))
    print(curPath)
    rootPath = curPath[:curPath.find("autotest\\") + len("autotest\\")]  # 获取myProject，也就是项目的根路径
    print(rootPath)










