#导入xlwt库用于写excel文件
import xlrd
import xlwt
import xlwt
import sys
import xdrlib ,sys
#初始化并创建一个工作簿
book = xlwt.Workbook()
#创建一个名为sheetname的表单
sheet = book.add_sheet('sheetname')
#在row_n行col_n列处单元格内写入value值

j = 1
k = 1
for i in range(15):
    for c in range(15):
        sheet.write(j,k,k+j)
        k = k+1
        print(k)
    j =j+1
    k =0



#将工作簿以bookname命名并保存
book.save('bookname.xls')



worksheet = xlrd.open_workbook('bookname.xls')
sheet_names= worksheet.sheet_names()#获取excel中所有工作表名
sheet2 = worksheet.sheet_by_name('sheetname')#根据Sheet名获取数据
sheet2 = worksheet.sheet_by_index(0)#根据索引获取数据，索引为0开始，1表示获取第二张工作表数据
#获取行数和列数

print('获取单元格A1值',sheet2.cell(3,4).value)

nrows = sheet2.nrows - 1
ncols = sheet2.ncols
print('行数',nrows)
print('列数',ncols)
rows = sheet2.row_values(1)   #表示获取Sheet2中第2行数据
print('获取Sheet2中第2行数据',rows)

cols10 = sheet2.col_values(2)   #表示获取Sheet2中第3列数据（数据保存为list）
print('获取Sheet2中第3列数据',cols10)

cell=sheet2.cell(0,1)   #表示获取Sheet2中(0,1)单元格的数据（数据保存为list）
print('获取Sheet2中(0,1)单元格的数据',cell)

print (sheet2.name,sheet2.nrows,sheet2.ncols)
#print (sheet2.cell(1,0).value.encode('utf-8'))

print ('ctype=',sheet2.cell(1,0).ctype)

print('获取单元格A1值',sheet2.cell(1,1).value)  #获取单元格A1值，column与row依然可用

for i in range(1,5,1):
    print(sheet2.cell(i,1).value) #更加方便实用
    c = sheet2.cell(i,1).value
    print(c)

    if c != 32:
        print("没有找到所需要的数")
    else:
        print("找到所需要的数")

