# encoding: utf-8
# @Time    : 2020/12/4 16:13
# @Author  : zhoubo
# @dsc     :
import pymysql
import configparser
from log.log import LogSet


_DB_CFG_PATH = "E:\PyProject\\autotest\conf.ini"
# 读取数据库配置
cf = configparser.ConfigParser()
cf.read(_DB_CFG_PATH)
HOST = cf.get("mysql_shenfu", "host")
PORT = cf.get("mysql_shenfu", "port")
USER = cf.get("mysql_shenfu", "user")
PASSWORD = cf.get("mysql_shenfu", "password")

@LogSet.get_log
class DataBase(object):
    # 连接mysql
    def __init__(self,db_name=''):
        try:
            self.connection = pymysql.connect(host=HOST,
                                              port=int(PORT),
                                              user=USER,
                                              password=PASSWORD,
                                              db=db_name,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            LogSet.error(f"Mysql connect fail:{e}\nDetail:host={HOST}, "
                         f"port={PORT}, user={USER}, passwd={PASSWORD}, db_name={db_name}")


    # 查询sql
    def query(self,sql) -> list:
        cur=self.connection.cursor()
        cur.execute(sql)
        resList=cur.fetchall()
        cur.close()
        return resList


    # 非查询的sql
    def execSql(self, sql) -> None:
        cur=self.connection.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()




if __name__ == '__main__':
    db = DataBase("scjrj_test")
    sql = "select * from bbd_test"
    r = db.query(sql)
    print(r)
    s = [i["id"] for i in r]
    print(s)

















