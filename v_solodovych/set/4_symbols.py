# 4. Напишіть функцію, яка приймає рядок символів (наприклад, "a14b6fh")
# і з використанням списків і множин визначає, чи всі символи в рядку унікальні.
def check_uniquity(symbols):
    symbols_list = list(symbols)
    symbols_set = set(symbols)

    if len(symbols_list) != len(symbols_set):
        return "Символи в рядку не є унікальними."
    else:
        return "Символи в рядку є унікальними."

symbols = input("Введіть рядок символів: ")

print(check_uniquity(symbols))