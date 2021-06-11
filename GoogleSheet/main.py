import gspread
gc = gspread.service_account(filename='/home/manikandan/Documents/API_Pytest/GoogleSheet/credentials.json')
sh = gc.open_by_key('12UblwURWwz6RACnCYbXxSFglM4jZgkwmL362f3pbJ7g')
worksheet = sh.sheet1
# res = worksheet.get_all_records()
# res = worksheet.get_all_values()
# res = worksheet.row_values(1)
# res = worksheet.col_values(1)
# res = worksheet.get('A2:C2')
user = ["Mani4", 27, "Egam"]
# worksheet.insert_row(user, 3)
worksheet.append_row(user)

# print(res)