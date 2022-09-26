import csv
import user_input

def add_info(path):
    name = user_input.ask_name()
    phone = user_input.ask_phone()
    newLine = [name, phone]
    with open(path, 'a', newline = '') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerow(newLine)

def find_num(path):
    name = user_input.ask_name()
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            if name == row[0]:
                print(*row)

def show_all(path):
    with open(path, 'r') as file:
       reader = csv.reader(file, delimiter = ';')
       for row in reader:
            print('{:<10} {:<15}'.format(*row))

def delete_item(path):
    name = user_input.ask_name()
    temp_list =[]
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            temp_list.append(row)
    for item in temp_list:
        if name in item:
            temp_list.remove(item)
            print('Запись удалена')
            break
    with open(path, 'w') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(temp_list)

def change_item(path):
    name = user_input.ask_name()
    temp_list =[]
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            temp_list.append(row)
    for item in temp_list:
        if name in item:
            print(item)
            temp_list.remove(item)
            name = user_input.ask_name()
            phone = user_input.ask_phone()
            newLine = [name, phone]
            temp_list.append(newLine)
            print('Запись изменена')
            break
    with open(path, 'w') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(temp_list)
