# -------------------------------------------
# Python MySQLdb 循环插入execute与批量插入executemany性能分析
# 插入数据量：10000条
# 每条字段：username, salt, pwd
# Author : Lrg
# -------------------------------------------
# encoding = utf-8

"""
pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(op)     执行一个数据库的查询命令
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
rowcount()      返回数据条数或影响行数
close()         关闭游标对象
"""


import xlrd
import time
import sys
import pymysql
import pymysql.cursors

# 从users.xls文件获取10000条用户数据
# 该文件由create_users.py生成

class Table1(object):
    def get_table(self,tablename):
        FILE_NAME = tablename
        data = xlrd.open_workbook(FILE_NAME)
        table = data.sheets()[0]
        return table

    # 读取Excel数据放在param中
    def read_tabledata(self,table):
        nrows = table.nrows
        param = []
        for i in range(1, nrows):
            # 第一列username，第二列salt，第三列pwd
            self.param.append([i, table.cell(i, 0).value, table.cell(i, 1).value, table.cell(i, 4).value,
                               table.cell(i, 5).value, table.cell(i, 6).value])

        return (param,nrows)


    # 连接数据库
    def readdatalib(self,param1, nrows1):
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="mysqltest",charset='utf8')
        cur = conn.cursor()

        # 新建数据库
        cur.execute('DROP TABLE IF EXISTS name1')
        sql = """CREATE TABLE name1(
                序号 CHAR(254),
                ERP代码 CHAR(254) NOT NULL,
                名称 CHAR(254),5
                规格型号 CHAR(255),
                物料属性 CHAR(255),
                计量单位 CHAR(255)
                )"""
        cur.execute(sql)


        #数据库插入数据
        try:
            sql = 'INSERT INTO name1 values(%s,%s,%s,%s,%s,%s)'
            # 批量插入
            cur.executemany(sql, param1)
            conn.commit()
            # 定义一个异常实例e
        except Exception as e:
            print
            e
            conn.rollback()
        print
        '[insert_by_many executemany] total:', nrows1 - 1

        # 释放数据连接
        if cur:
                cur.close()
        if conn:
                conn.close()



tt = Table1()
YY = tt.get_table("KingdeeExpImp80.xls")

(param1, nrows1) = tt.readdatalib(YY)
print(nrows1)
bb = "yy"
tt.readdatalib( param1, 11)