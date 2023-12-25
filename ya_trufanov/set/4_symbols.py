# 4. Напишіть функцію, яка приймає рядок символів (наприклад, "a14b6fh")
# і з використанням списків і множин визначає, чи всі символи в рядку унікальні.


def check_unique_str(value):
    list_symbols = list(value)
    set_symbols = set(value)

    if len(list_symbols) == len(set_symbols):
        print("Всі символи в рядку унікальні")
    else:
        print("Є повторюючі символи.")


user_string = "a14b6fh"
check_unique_str(user_string)
