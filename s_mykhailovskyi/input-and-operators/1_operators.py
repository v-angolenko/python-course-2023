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

firstnum = int(input("Введіть перше число:\n"))
secondnum = int(input("Введіть друге число:\n"))

sum = firstnum + secondnum
difference = firstnum - secondnum
multiplication = firstnum * secondnum
division = firstnum / secondnum

print(f'{firstnum} + {secondnum} = {sum}')
print(f'{firstnum} - {secondnum} = {difference}')
print(f'{firstnum} * {secondnum} = {multiplication}')
print(f'{firstnum} / {secondnum} = {division}')