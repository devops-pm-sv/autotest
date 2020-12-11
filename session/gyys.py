# encoding: utf-8
# @Time    : 2020/12/11 16:29
# @Author  : zhoubo
# @dsc     : 贵阳营商系统session
import requests
import json
from log.log import LogSet
import hashlib


# 贵阳营商session
@LogSet.get_log
class Session_gyys():

    @classmethod
    def _md5(self,passwd):
        return hashlib.md5(passwd.encode()).hexdigest()


    @staticmethod
    def session_front(user, passwd):
        '''前台系统session'''
        url = "http://gyys.bbdservice.net/gyys/api/v1.0/user/login"
        session = requests.session()
        data = {"userAccount": user, "passwords": Session_gyys._md5(passwd)}
        headers = {"Content-Type": "application/json"}
        session.post(url=url, data=json.dumps(data), headers=headers)
        return session





if __name__ == '__main__':
    session = Session_gyys.session_front("贵阳市营商办2","123456")
    # 测试session
    rr = session.get(url="http://gyys.bbdservice.net/gyys/api/v1.0/affair-mgt/query-departments")
    print(rr.text)


















