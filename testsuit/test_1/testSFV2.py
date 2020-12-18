# encoding: utf-8
# @Time    : 2020/12/18 16:26
# @Author  : zhoubo
# @dsc     :
import unittest
import json
import requests
from log.log import LogSet



class SFV2Case(unittest.TestCase):

    def setUp(self) -> None:
        url = "http://ieadmin.feicheng.com/shantoucredit_govuser/security/tokenadmin"
        data = {"username": "QWE", "password": "123456"}
        headers = {"Content-Type": "application/json"}
        sess = requests.session()
        r = sess.post(url=url,data=json.dumps(data),headers=headers)
        res = json.loads(r.text)
        token = res["data"]["token"]
        global headers1
        headers1 = {"token": token}



    def test1(self):
        url1 = 'http://ieadmin.feicheng.com/shantoucredit_govuser/access/getMyAccessView?_=1608276571256'
        rr = requests.get(url=url1,headers=headers1)
        print(rr.text)
































