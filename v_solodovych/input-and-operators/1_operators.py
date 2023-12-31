# Тема: Арифметичні оператори та ввод даних через `input`.

# Завдання:
# Напишіть програму, яка запитує у користувача два числа через `input()`.
# Програма повинна виконувати базові арифметичні операції (додавання, віднімання, множення, ділення)
# з цими числами і виводити результати на екран.

a = int(input("\nВведіть перше число: "))
b = int(input("Введіть друге число: "))

c = [a+b, a-b, a*b, a/b]

print(f"\nРезультати:\n{a} + {b} = {c[0]} \n{a} - {b} = {c[1]} \n{a} * {b} = {c[2]} \n{a} \ {b} = {c[3]}\n")

# Очікуваний результат:
# ```
# Введіть перше число: 5
# Введіть друге число: 3

# Результати:
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 3 = 1.6666666666666667
