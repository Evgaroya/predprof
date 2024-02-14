import csv

with open('vacancy.csv', encoding = 'utf-8 with bom') as file:
    reader = list(csv.DictReader(file, delimiter = ';', quotechar='"')
    for i in range(len(reader)):
        cursor = reader[i]
        pos = i
        while pos > 0 and int(reader[pos - 1]['company_size'] < cursor_company_size:
            reader[pos] = reader[pos - 1]
            pos = pos - 1
        reader[pos] = cursor
    for salary, work_Type, company_Size, role, company in reader:

count = 1
for 