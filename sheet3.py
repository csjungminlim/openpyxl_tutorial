# sheet3.py

import openpyxl

book = openpyxl.load_workbook('sheets.xlsx')

sheet = book.get_sheet_by_name("March")
sheet.sheet_properties.tabColor = "0072BA"

book.save('sheets3.xlsx')
