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
import xlrd
import xlwt
def readTabel(i):

        worksheet = xlrd.open_workbook('KingdeeExpImp80.xls')
        sheet_names = worksheet.sheet_names()
        # 根据索引获取数据，索引为0开始，1表示获取第二张工作表数据
        sheet2 = worksheet.sheet_by_index(0)

        # 获取行数和列数
        nrows = sheet2.nrows - 1
        ncols = sheet2.ncols
        print('行数', nrows)
        print('列数', ncols)
        # 表示获取Sheet2中第2行数据
        rows = sheet2.row_values(1)
        print('获取Sheet2中第2行数据', rows)

        cell0 = sheet2.cell(i, 0).value
        cell1 = sheet2.cell(i, 1).value
        cell4 = sheet2.cell(i, 4).value
        cell5 = sheet2.cell(i, 5).value
        cell6 = sheet2.cell(i, 6).value
        print('获取Sheet2中(1,0)单元格的数据', cell0)
        print('获取Sheet2中(1,1)单元格的数据', cell1)
        print('获取Sheet2中(1,4)单元格的数据', cell4)
        print('获取Sheet2中(1,5)单元格的数据', cell5)
        print('获取Sheet2中(1,6)单元格的数据', cell6)
        sum = (cell0, cell1, cell4, cell5, cell6,"","","","")
        return  sum

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

# 删除数据
sql = "DELETE FROM erp1 WHERE marks = '%s' LIMIT %d"
data = ("", 1000)
cursor.execute(sql % data)
connect.commit()
print('成功删除', cursor.rowcount, '条数据')




# 插入数据
sql = "INSERT INTO erp1 (name, ERPcode,specs,type1,unit,price,maker,ph,marks) VALUES" \
      " (  '%s','%s','%s','%s','%s','%s','%s','%s','%s' )"


j = 1
k = 1
for i in range(1):
        sum1 = readTabel(i)
        print(sum1[0])
        cursor.execute(sql % sum1)
        connect.commit()
        print('成功插入', cursor.rowcount, '条数据')
        k = k+1

# 关闭连接
cursor.close()
connect.close()