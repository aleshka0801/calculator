# Controller.py

from model import *
from view import *

def main():
    while True:
        choice = display_menu()

        if choice == "1":
            a, b = get_numbers()
            result = add(a, b)
            show_result(result)
        elif choice == "2":
            a, b = get_numbers()
            result = subtract(a, b)
            show_result(result)
        elif choice == "3":
            a, b = get_numbers()
            result = multiply(a, b)
            show_result(result)
        elif choice == "4":
            a, b = get_numbers()
            try:
                result = divide(a, b)
                show_result(result)
            except ValueError as e:
                show_message(str(e))
        elif choice == "0":
            show_message("Пока!")
            break
        else:
            show_message("Неверный выбор, попробуй снова")

if __name__ == "__main__":
    main()