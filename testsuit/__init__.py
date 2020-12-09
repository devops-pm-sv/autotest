# encoding: utf-8
# @Time    : 2020/12/4 11:30
# @Author  : zhoubo
# @dsc     :
import sys
import unittest
class Aeest(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.case_result = False

    @classmethod
    def set_pass(self, msg='') -> None:
        sys.stdout.write(msg)

    @classmethod
    def set_fail(self, msg="测试失败!") -> None:
        raise Aeest.failureException(msg)
