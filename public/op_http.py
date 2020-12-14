# encoding: utf-8
# @Time    : 2020/12/14 10:12
# @Author  : zhoubo
# @dsc     :
import requests
from log.log import LogSet
from session.gyys import Session_gyys


@LogSet.get_log
class Http:
    def __init__(self, session=None):
        self.session = session

    def _sess_request(self, url, method, data, **kwargs):
        '''请求需要session'''
        if method=="get":
            res = self.session.request(url=url, method=method, params=data, **kwargs)
        elif method=="post":
            res = self.session.request(url=url, method=method, data=data, **kwargs)
        else:
            LogSet.error(msg=f"暂未封装该方法：{method}")
            return
        return res


    def _without_sess_request(self, url, method, data, **kwargs):
        '''请求不需session'''
        if method=="get":
            res = requests.request(url=url, method=method, params=data, **kwargs)
        elif method=="post":
            res = requests.request(url=url, method=method, data=data, **kwargs)
        else:
            LogSet.error(msg=f"暂未封装该方法：{method}")
            return
        return res


    def http(self, url, method, data, **kwargs):
        '''http请求'''
        if self.session==None:
            return self._without_sess_request(url, method, data, **kwargs)
        else:
            return self._sess_request(url, method, data, **kwargs)





if __name__ == '__main__':
    # session = Session_gyys.session_front("贵阳市营商办2","123456")
    # h = Http(session)
    # url = "http://gyys.bbdservice.net/gyys/api/v1.0/affair-mgt/query-departments"
    # method = "get"
    # data = ''
    # r = h.http(url, method, data)
    # print(r)

    url = "http://credit.feicheng.com/shantoucredit_pubserver/dataService/getTypeid"
    h = Http().http(url=url,method="get",data='')
    print(h.text)
    print(h)






















