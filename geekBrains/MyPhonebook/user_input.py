def menu():
    return input("""
    Меню: 

    1. Добавить контакт
    2. Найти контакт
    3. Удалить контакт
    4. Показать все
    5. Изменить контакт

    Что делаем? """)

def ask_name():
    return input('Имя: ')

def ask_phone():
    return input('Телефон: ')

def error():
    print("Выберите действие 1-5")
