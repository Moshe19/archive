import xlsxwriter
from sk_mvideo import arrey

def writer(parametr):
    book = xlsxwriter.Workbook(r'C:\Users\admin\Desktop\Обучение python\Скрапинг сайта\data.xlsx')
    page = book.add_worksheet('авто_глазов')
    
    row = 0
    column = 0
    
    page.set_column('A:A', 50)
    page.set_column('B:B', 50)
    page.set_column('C:C', 50)
    page.set_column('D:D', 50)
    
    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        row += 1
        
    book.close()

writer(arrey)    