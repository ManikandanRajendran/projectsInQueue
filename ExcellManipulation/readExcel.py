import openpyxl

wb = openpyxl.load_workbook('/home/manikandan/Documents/API_Pytest/ExcellManipulation/pricingSheet.xlsx')

sheet = wb.active

print(sheet)

# wb.save('/home/manikandan/Documents/API_Pytest/ExcellManipulation/test.xlsx')