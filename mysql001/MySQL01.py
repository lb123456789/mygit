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
class MySQLBuilder :

    def MySQL_connect(self):  # 创建数据库连接
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='mysqltest',
            charset='utf8'

        )

        # 获取游标
        self.cursor = connect.cursor()

    def MySQL_createTable(self):  # 创建表单
        self.cursor.execute('DROP TABLE IF EXISTS name1')
        sql = """CREATE TABLE name1(
                        序号 CHAR(254),
                        ERP代码 CHAR(254) NOT NULL,
                        名称 CHAR(254),
                        规格型号 CHAR(255),
                        物料属性 CHAR(255),
                        计量单位 CHAR(255)
                        )"""
        self.cursor.execute(sql)

    def MySQL_inserInto(self, name1, param, nrows):  # 插入数据

        try:
            sql = 'INSERT INTO name1 values(%s,%s,%s,%s,%s,%s)'
            # 批量插入
            self.cursor.executemany(sql, param)
            self.cursor.commit()
            # 定义一个异常实例e
        except Exception as e:
            print
            e
            self.cursor.rollback()
        print
        '[insert_by_many executemany] total:', nrows - 1

    def MySQL_upDate(self, data):  # 修改数据
        sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
        self.cursor.execute(sql % data)
        self.connect.commit()
        print('成功修改', self.cursor.rowcount, '条数据')

    def MySQL_select(self, data):  # 查询数据
        sql = "SELECT name,saving FROM trade WHERE account = '%s' "
        self.cursor.execute(sql % data)
        for row in self.cursor.fetchall():
            print("Name:%s\tSaving:%.2f" % row)
        print('共查找出', self.cursor.rowcount, '条数据')
    def MySQL_delete(self,data):  # 删除数据
        # 删除数据
        sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
        self.cursor.execute(sql % data)
        self.connect.commit()
        print('成功删除', self.cursor.rowcount, '条数据')
        pass

