#coding=utf-8
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
import pymysql



class MysqlOperation:
    def __init__(self, host='localhost', port=3306, db='mysqltest', user='root', passwd='root', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
    print("OK")
    # 插入一条数据
    def insert(self, sql, params):
        return self.__cud(sql,params)

    # 修改一条数据
    def update(self, sql, params):
        return self.__cud(sql, params)

    # 删除一条数据
    def delete(self, sql, params):
        return self.__cud(sql, params)

    def __cud(self, sql, params=[]):
        try:
            cs1 = self.conn.cursor()
            rows = cs1.execute(sql % params)
            self.conn.commit()
            return rows
        except Exception as e:
            print(e)
            self.conn.rollback()
        cs1.close()
        self.conn.close()

    def fetchone(self, sql, params=[]):
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql % params)
            row = cs1.fetchone()
            return row
        except Exception as e:
            print(e)
        cs1.close()
        self.conn.close()

    def fetchall(self, sql, params):
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql % params)
            rows = cs1.fetchall()
            return rows
        except Exception as e:
            print(e)
        cs1.close()
        self.conn.close()
if __name__ == "__main__":
    A = MysqlOperation()

    # 插入一条数据
    AA = '雷军'
    BB = '13512348866'
    CC = 588
    DD = 555
    EE = 555
    sql1 = "INSERT INTO trade (name, account, saving,expend,income) VALUES ( '%s', '%s', %.2f ,%.2f ,%.2f )"
    data1 =(AA, BB, CC ,DD, EE)


    # 将caaount=13512345645一行字段为saving修改为8000
    sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
    data = (8000, '13512345645')


    # 删除account=13512345645,其中10条数据
    sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
    data = ('13512345645', 10)
    A.update(sql, data)


    sql = "SELECT name,saving FROM trade WHERE account = '%s' "
    data = ('13512348866',)

    dd =A.fetchone(sql, data)
    print(dd)

    ff = A.fetchall(sql, data)
    print(ff)