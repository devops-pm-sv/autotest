# encoding: utf-8
# @Time    : 2020/12/4 16:13
# @Author  : zhoubo
# @dsc     :
import pymysql
import configparser
from autotest.log.log import LogSet

_db_cfg_path = "E:\PyProject\\autotest\conf.ini"
# 读取数据库配置
cf = configparser.ConfigParser()
cf.read(_db_cfg_path)
HOST = cf.get("mysql_shenfu", "host")
PORT = cf.get("mysql_shenfu", "port")
USER = cf.get("mysql_shenfu", "user")
PASSWORD = cf.get("mysql_shenfu", "password")


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
            LogSet.error(f"Mysql connect fail:{e}\nDetail:host={HOST}, port={PORT}, user={USER}, passwd={PASSWORD}, db_name={db_name}")

    # 清除table_name中的数据
    # def clear(self, db_name,table_name):
    #     DB.__init__(self,db_name)
    #     # real_sql = "truncate table " + table_name + ";"
    #     real_sql = "delete from " + table_name + ";"
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    #         cursor.execute(real_sql)
    #     self.connection.commit()

    # 向table中插入数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    # 查询table_name返回特定字段的值
    # def query(self,db_name,sql,sqlField):
    #     DB.__init__(self, db_name)
    #     # real_sql = "select * from " + tabale_name+ " where "+condition+";"
    #     real_sql = sql
    #     print(real_sql)
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(real_sql)
    #         results = cursor.fetchall()#获取所有查询结果
    #         # print(type(results))
    #         # print(results)
    #         reusem = reuse_methods.REUSEMETHODS()
    #         field_value = reusem.get_target_value(key=sqlField,dic_tmp=results,data_list=[])#获取特定字段的值写入列表
    #         # print(type(field_value))
    #         # print(field_value)
    #         # print(field_value[0])
    #     self.connection.commit()
    #     return field_value

    # 删除table表中的特定行(依据id 或 nid来操作)
    # def delete(self, db_name, table_name, id,num):
    #     DB.__init__(self, db_name)
    #     # real_sql = "select * from " + tabale_name+ " where "+condition+";"
    #     # select * from timer where id = 6
    #
    #     # DELETE * FROM TABLE where id = 1
    #
    #     real_sql = "DELETE FROM {tablename} where {id} = {num};"
    #     real_sql = real_sql.format(tablename=table_name,id=id,num=num)
    #
    #     # print (real_sql)
    #     with self.connection.cursor() as cursor:
    #         # cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    #         cursor.execute(real_sql)
    #     self.connection.commit()
    #
    # # 删除table表中的特定行(依据type来操作)
    # def delete_systemconfig(self):
    #     DB.__init__(self, 'auto_basic')
    #     # real_sql = "select * from " + tabale_name+ " where "+condition+";"
    #     # select * from timer where id = 6
    #
    #     # DELETE * FROM TABLE where id = 1
    #
    #     real_sql = "DELETE FROM `basic_config` where config_type = 'old';"
    #
    #     print (real_sql)
    #
    #     with self.connection.cursor() as cursor:
    #         # cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    #         cursor.execute(real_sql)
    #     self.connection.commit()
    #
    # #删除table中的部分数据
    # def delete_partialLineDate(self,db_name,table_name,field_title,reserved_fields):
    #     DB.__init__(self,db_name)
    #     real_sql = "DELETE FROM "+table_name+" WHERE "+field_title+" NOT IN "+reserved_fields+";"
    #     # print(real_sql)
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("SET FOREIGN_KEY_CHECKS=0;")#关闭外键约束
    #         cursor.execute(real_sql)
    #         cursor.execute("SET FOREIGN_KEY_CHECKS=1;")#打开外键约束
    #     self.connection.commit()
    #
    #
    # # 关闭数据库连接
    # def close(self):
    #     self.connection.close()
    #
    # # 初始化数据
    # def init_data(self, tabale_name):
    #     # for table, data in datas.items():
    #     #     self.clear(table)
    #     #     for d in data:
    #     #         self.insert(table, d)
    #     # self.close()
    #     self.__init__()
    #     self.clear(self.tabale_name)
    #     self.close()



if __name__ == '__main__':
    db = DataBase("scjrj_test")


















