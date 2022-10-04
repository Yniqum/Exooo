# import json
# import csv
# import openpyxl

'''task 1 - json'''

# data = {
#     'First name': 'Dmitry',
#     'Last name': 'Sidorov',
#     'Age': '33',
# }
#
# with open('data.json', 'w') as file:
#     json.dump(data, file)

'''task 1 - csv'''

# myData = [["first_name", "Last_name", "Age"],
#           ['Dmitry', 'Sidorov', '33']]
#
# myFile = open('data.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)

'''task 1 - excel'''

# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
# ws.title = "Data"
# ws['A1'] = "first_name"
# ws['B1'] = "Last_name"
# ws['C1'] = "Age"
# ws['A2'] = "Dmitry"
# ws['B2'] = "Sidorov"
# ws['C2'] = "33"
# wb.save('test.xlsx')

'''task 2'''
#
# my_file = open("Doc.txt", "w+")
# my_file.write("Мой, файл!")
# my_file.close()
# my_file = open("Doc.txt", "a+")
# my_file.write("Добавить ещё это к моему файлу!")
# my_file.close()
