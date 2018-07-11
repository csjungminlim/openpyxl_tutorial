# iterating-by_rows.property
# -*- coding: utf-8 -*-

from openpyxl import Workbook

book = Workbook()
sheet = book.active

rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

for row in rows:
    sheet.append(row)

for row in sheet.iter_rows(min_row=1, min_col=1, max_row=6, max_col=3):
    for cell in row:
        print cell.value, # python2에선 print(~, end=" ") 대신 ,로 사용(줄바꿈 제거)
    print ''

book.save('iterbyrows.xlsx')
