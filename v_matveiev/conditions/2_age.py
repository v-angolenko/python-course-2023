# Тема:
# Обробка користувацького вводу та умовні оператори if-elif-else

# Завдання:
# Створіть програму, яка запитує у користувача ввести його вік (змінна `age`).
# На основі введеного віку програма має визначити та вивести етап життя користувача. Визначення етапів життя:

# - Якщо вік менше 18, вивести: "Ви - підліток."
# - Якщо вік від 18 до 65 (включно), вивести: "Ви - дорослий."
# - Якщо вік більше 65, вивести: "Ви - пенсіонер."

# Переконайтесь, що програма коректно обробляє некоректні вводи, наприклад,0
# від'ємні числа або нечислові значення, виводячи повідомлення: "Некоректний ввод.
# Будь ласка, введіть дійсний вік."

# Очікуваний результат:
# Програма запитує у користувача ввести його вік і в залежності від введеного числа
# виводить відповідне повідомлення про етап життя, або ж повідомлення про помилку у випадку некоректного вводу.

age = int(input('Введіть ваш вік: '))
if age > 65:
    print ('Ви - пенсіонер.')
elif 18 < age <= 65:
    print ('Ви - дорослий.')
elif 12 < age < 18:
    print ('Ви - підліток.')
else:
    print ('Некоректний ввод. Будь ласка, введіть дійсний вік.')