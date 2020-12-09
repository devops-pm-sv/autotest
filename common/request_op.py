# encoding: utf-8
# @Time    : 2020/12/4 11:29
# @Author  : zhoubo
# @dsc     :
from autotest.log.log import LogSet

@LogSet.get_log
class Other():

    def tt(self,m,s=0):
        print("测试公共库","1+1",s,m)
        Other().tr()
        # d=p


    def tr(self):
        print("trtrrtt")


