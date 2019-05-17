# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         CreatTbable
# Description:
# Author:       Administrator
# Date:         2019/5/7
# 文件注解：创建excel表格，输入的写入excel，Excel的查找，Excel单元格数据读取
# -------------------------------------------------------------------------------


# 导入xlwt库用于写excel文件
import xlrd
import xlwt
# 初始化并创建一个工作簿
book = xlwt.Workbook()
# 创建一个名为sheetname的表单
sheet = book.add_sheet('sheetname')
# 在row_n行col_n列处单元格内写入value值

j = 1
k = 1
for i in range(50):
    for c in range(50):
        sheet.write(j, k, "易欢")
        k = k+1
        print(k)
    j = j+1
    k = 1
# 将工作簿以bookname命名并保存
book.save('bookname.xls')

# Excel中数据的读取查找
worksheet = xlrd.open_workbook('KingdeeExpImp80.xls')
# 获取excel中所有工作表名
sheet_names = worksheet.sheet_names()
# 根据Sheet名获取数据
sheet2 = worksheet.sheet_by_name('KingdeeExpImp80')
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

# 表示获取Sheet2中第3列数据（数据保存为list）
cols10 = sheet2.col_values(2)
print('获取Sheet2中第3列数据', cols10)

# 表示获取Sheet2中(0,1)单元格的数据（数据保存为list）
cell=sheet2.cell(0, 1)
print('获取Sheet2中(0,1)单元格的数据', cell)

print (sheet2.name, sheet2.nrows, sheet2.ncols)
# print (sheet2.cell(1,0).value.encode('utf-8'))

print('ctype=', sheet2.cell(1, 0).ctype)

# 获取单元格A1值，column与row依然可用
print('获取单元格A1值', sheet2.cell(1, 1).value)

# 查找一个数据并打印出
for i in range(1, 5, 1):
    print(sheet2.cell(i, 1).value)
    c = sheet2.cell(i, 1).value
    print(c)

    if c != 4:
        print("没有找到所需要的数")
    else:
        print("找到所需要的数")

