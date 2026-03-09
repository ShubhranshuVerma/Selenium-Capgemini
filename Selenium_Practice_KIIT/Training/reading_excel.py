import xlrd
path=r'/Users/shubhranshuverma/PycharmProjects/Selenium_Training/Files/Book.xlsx'

##open the excel
workbook=xlrd.open_workbook(path)

##open wokrsheet
worksheet=workbook.sheet_by_name("Sheet1")

##convert sheet object to generator object
rows=worksheet.get_rows()

##print only values
for row in rows:
    print(row[0].value,row[1].value,row[2].value,row[3].value,row[4].value)


