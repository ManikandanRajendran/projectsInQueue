import csv, random
with open('static/data.csv', 'r') as file:
        # reader = csv.reader(file)
        # row_count = sum(1 for row in reader)
        # num = random.randrange(row_count)
        # print(num)
        # file.seek(num)
        # print(file.readline())
        # reader = csv.reader(file)
        # chosen_row = random.choice(list(reader))
        # print(chosen_row)
        lines = sum(1 for line in file)
        line_number = random.randrange(lines)
        print(line_number)
