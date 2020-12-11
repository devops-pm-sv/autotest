# encoding: utf-8
# @Time    : 2020/12/11 16:09
# @Author  : zhoubo
# @dsc     :红警系统的session
import requests
import json
from log.log import LogSet
import hashlib



@LogSet.get_log
class Session_Red(object):

    @classmethod
    def _md5(self,passwd):
        return hashlib.md5(passwd.encode()).hexdigest()



    @staticmethod
    def session_red(user, passwd):
        '''返回session对象：红警系统的seeion'''

        url = "http://red-alert.testing.bbdops.com/api/v1.0/auth/sso/login?t=370230"
        data = {"username": user, "password": Session_Red._md5(passwd), "systemState": 1, "location": "四川省成都市"}
        headers = {"Content-Type": "application/json"}
        sess = requests.session()
        sess.post(url=url,data=json.dumps(data),headers=headers)
        return sess




if __name__ == '__main__':
    # 获取session
    ssee = Session_Red.session_red("zhoubo","123456+Y")
    # 测试session
    url1 = "http://red-alert.testing.bbdops.com/api/v1.0/company/info/search-company"
    data1 = {"key":"小米", "pageNum":1, "pageSize":1, "type":"综合", "t":334005, "currentPageName":"智能检索分析"}
    headers1 = {"Referer":"http://red-alert.testing.bbdops.com/signin/"}
    m = ssee.get(url=url1,params=data1,headers=headers1)
    print(m.text)











