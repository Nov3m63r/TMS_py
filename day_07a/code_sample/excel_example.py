import openpyxl
wb = openpyxl.load_workbook(filename='table.xlsx')
sheet = wb['Лист1']
print(sheet)

print(sheet['A2'].value)
print([v[0].value for v in sheet['A2':'A6']])

sheet['A2'] = 'John'
print(sheet['A2'].value)
wb.save('table2.xlsx')
