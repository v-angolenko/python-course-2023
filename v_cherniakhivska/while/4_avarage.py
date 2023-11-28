# Тема: Цикли while з використанням input для обчислення середнього значення

# Завдання:
# Створіть програму, яка обчислює середнє арифметичне введених користувачем позитивних чисел.
# Програма має запитувати у користувача ввести число, додаючи введене число до загальної суми і
# збільшуючи лічильник введених чисел до тих пір, поки користувач не введе "0". Коли введено "0",
# програма повинна вивести середнє арифметичне усіх введених до того чисел.

# Очікуваний результат:
# Якщо користувач вводить числа 4, 5, 6, 0 послідовно, програма повинна вивести:
# ```
# Введіть число або "0" для завершення: 4
# Введіть число або "0" для завершення: 5
# Введіть число або "0" для завершення: 6
# Введіть число або "0" для завершення: 0
# Середнє значення введених чисел: 5.0
# ```

# Послідовність виконання:
# 1. Ініціалізуйте змінну для збереження суми введених чисел (sum_of_numbers) зі значенням 0.
# 2. Ініціалізуйте змінну для підрахунку кількості введених чисел (count_of_numbers) зі значенням 0.
# 3. Встановіть цикл while, який продовжує працювати, поки не буде введено "0".
# 4. Отримайте число від користувача і перевірте, чи воно не дорівнює "0".
# 5. Якщо число не дорівнює "0", додайте його до суми та збільшіть лічильник.
# 6. Якщо введено "0", обчисліть і виведіть середнє арифметичне введених чисел,
# поділивши суму на кількість введених чисел (не враховуючи нуль).
# 7. Виведіть результат і завершіть програму.

# Можна використати
# while True:
#   ...
#   break;

sum_of_numbers = 0
count_of_numbers = 0
user_input=""
while True:
    user_input = input("Введіть число: ")
    if user_input == "0":
        break
    else:
        b = int(user_input)
    if b > 0:
        sum_of_numbers += b
        count_of_numbers += 1
print("Сума",sum_of_numbers,"Кількість",count_of_numbers)
