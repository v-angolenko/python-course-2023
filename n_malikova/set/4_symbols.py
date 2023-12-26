# 4. Напишіть функцію, яка приймає рядок символів (наприклад, "a14b6fh")
# і з використанням списків і множин визначає, чи всі символи в рядку унікальні.

def are_all_characters_unique(input_string):
    seen_chars = set()
    for char in input_string:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True
input_str = input("Введіть текст: ")
result = are_all_characters_unique(input_str)
print("Чи всі символи унікальні: ", result)
