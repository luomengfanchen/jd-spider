import openpyxl
from rich import print as rprint

wb = openpyxl.Workbook()
ws = wb.active

# 将数据保存到名为data.xlsx的excel表格中
def save_data(good_datas):
    for item in good_datas:
        ws.append(item)

    wb.save('data.xlsx')
    rprint('[bold red]' + '>>>数据存入xlsx成功' + '[/bold red]')
