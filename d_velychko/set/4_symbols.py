# 4. Напишіть функцію, яка приймає рядок символів (наприклад, "a14b6fh")
# і з використанням списків і множин визначає, чи всі символи в рядку унікальні.

def are_all_characters_unique(input_string):
    unique_chars = []

    for char in input_string:
        if char in unique_chars:
            return False
        else:
            unique_chars.append(char)

    return True

input_str = "a14b6fh"
result = are_all_characters_unique(input_str)
if result:
    print("Всі символи унікальні в рядку", input_str)
else:
    print("Не всі символи унікальні в рядку", input_str)
