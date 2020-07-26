import xlrd
import xlwt

'''
读/写 Excel文件

xlrd 读 
xlwt 写

'''

book = xlrd.open_workbook('/Users/hjd/Downloads/Untitled.xlsx')

#列出工作表
for sheet in book.sheets():
    print(sheet.name)

#读取工作表
sheet = book.sheet_by_name('Sheet1')

#打印工作表所有行
for i in range(sheet.nrows):
    print(sheet.row_values(i))

