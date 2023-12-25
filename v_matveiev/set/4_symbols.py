# 4. Напишіть функцію, яка приймає рядок символів (наприклад, "a14b6fh")
# і з використанням списків і множин визначає, чи всі символи в рядку унікальні.
def i(s):
    char_set = set() 

    for char in s:
        if char in char_set:
            return False 
        char_set.add(char) 

    return True 
input_string = input("Введіть рядок символів: ")
result = i(input_string)
print("Усі символи унікальні:", result)
