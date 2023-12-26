# Тема: Арифметичні оператори та ввод даних через `input`.

# Завдання:
# Напишіть програму, яка запитує у користувача два числа через `input()`.
# Програма повинна виконувати базові арифметичні операції (додавання, віднімання, множення, ділення)
# з цими числами і виводити результати на екран.

# Очікуваний результат:
# ```
# Введіть перше число: 5
# Введіть друге число: 3

# Результати:
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 3 = 1.6666666666666667

first_number = float(input("Введіть перше число: "))
second_number = float(input("Введіть друге число: "))
print("Результат: ")
print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")
print(f"{first_number} / {second_number} = {first_number / second_number}")
