# View.py

def display_menu():
    print("\nВыбери действие: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление, 0 - выход")
    choice = input("Введи номер действия: ")
    return choice

def get_numbers():
    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))
    return a, b

def show_result(result):
    print(f"Результат: {result}")

def show_message(message):
    print(message)