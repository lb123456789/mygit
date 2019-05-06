"""
1） 打开工作表：

代码如下:

import xlrd
wb = xlrd.open_workbook('workbook_name')
wb = xlrd.open_workbook(file_contents = data)

2） 检查工作表名称，获取工作表：

代码如下:

wb.sheet_names()
sh = wb.sheet_by_index(0)
sh = wb.sheet_by_name(u'Sheet1')

3） 查询数据：

i. 获取行数，列数：

代码如下:

rows = sh.rows
cols = sh.cols

ii. 查询行数据：

代码如下:

sh.row_values(row_num)

iii. 查询列数据：

代码如下:

sh.row_values(col_num)

iv. 查询单元格数据：

代码如下:

sh.cel(row_num, col_num).value
"""