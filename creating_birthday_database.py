import csv
import openpyxl
from openpyxl import load_workbook

csv_data=[]
with open('Contacts.csv') as file_obj:
    reader=csv.reader(file_obj)
    for row in reader:
        csv_data.append(row)
wb=openpyxl.Workbook()
sheet=wb.active
for row in csv_data:
    sheet.append(row)
ws=wb.active
ws.delete_cols(2,11)
ws.delete_cols(3,18)
ws.delete_cols(4,18)

wb.save('bdays.xlsx')

