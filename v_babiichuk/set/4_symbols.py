# 4. Напишіть функцію, яка приймає рядок символів (наприклад, "a14b6fh")
# і з використанням списків і множин визначає, чи всі символи в рядку унікальні.
def check_unique_symbols(value):
    list_symbols = list(value)
    set_symbols = set(value)

    return len(list_symbols) == len(set_symbols)


user_string = input("Введіть рядок: ")
result = check_unique_symbols(user_string)

if result:
    print("Всі символи в рядку унікальні.")
else:
    print("Є повторюючі символи.")