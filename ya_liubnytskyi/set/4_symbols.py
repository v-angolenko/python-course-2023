# 4. Напишіть функцію, яка приймає рядок символів (наприклад, "a14b6fh")
# і з використанням списків і множин визначає, чи всі символи в рядку унікальні.
def unique_symbol(user_string):
    if len(set(user_string)) == len(list(user_string)):
        print("Всі символи в рядку унікальні.")
    else:
        print("Є символи які повторюються ")
    

user_string = "a14b6fh"
unique_symbol(user_string)
    