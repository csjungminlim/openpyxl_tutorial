#appending_values.py

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

book.save('appending.xlsx')
