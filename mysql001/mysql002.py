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
import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='mysqltest',
    charset='utf8'

)

# 获取游标
cursor = connect.cursor()

# 插入数据
sql = "INSERT INTO erp1 (name, account, saving,expend,income) VALUES ( '%s', '%s', %.2f ,%.2f ,%.2f )"
data = ('雷军', '18012345678', 10000,6000,8000)
cursor.execute(sql % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')


# 关闭连接
cursor.close()
connect.close()