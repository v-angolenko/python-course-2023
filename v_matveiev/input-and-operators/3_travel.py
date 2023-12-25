# ```
# Тема: Арифметичні оператори та обробка введення користувача.

# Завдання:
# Напишіть програму, яка дозволяє користувачу ввести кількість кілометрів,
# які він планує пройти в похід, та середню швидкість пересування в кілометрах за годину.
# Програма має обрахувати і вивести на екран час (у годинах та хвилинах), який знадобиться користувачу,
# щоб пройти заплановану відстань.

# Очікуваний результат:
# ```
# Введіть кількість кілометрів для походу: 20
# Введіть вашу середню швидкість (км/год): 5

# Час необхідний для проходження відстані: 4 години та 0 хвилин.
# ```
distance = float(input("Введіть кількість кілометрів для походу: "))
speed = float(input("Введіть вашу середню швидкість (км/год): "))
time_in_hours = distance / speed
hours = int(time_in_hours)
minutes = int((time_in_hours - hours) * 60)
print(f"Час необхідний для проходження відстані: {hours} години та {minutes} хвилин.")
