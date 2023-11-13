# Тема: Цикли while з використанням input

# Завдання:
# Створіть програму, яка використовує цикл while для зчитування чисел, введених користувачем,
# доки не буде введено "stop".
#
# Після кожного введення, програма повинна виводити повідомлення "Число прийнято" і продовжувати роботу.
# Коли користувач введе "stop", програма має вивести суму всіх введених доти чисел.

# Очікуваний результат:
# Припустимо, користувач послідовно вводить "5", "3", "8", "stop", програма повинна вивести:
# ```
# Число прийнято
# Число прийнято
# Число прийнято
# Сума введених чисел: 16
# ```

# Послідовність виконання:
# 1. Ініціалізуйте змінну для збереження суми введених чисел (total_sum) зі значенням 0 і пусту змінну user_input.
# 2. Ініціалізуйте цикл while, який працює до тих пір, поки змінна (user_input) не дорівнює "stop".
# 3. Всередині циклу, отримайте введення від користувача.
# 4. Перевірте, чи введений рядок дорівнює "stop". Якщо так, вийдіть з циклу.
# 5. Якщо введений рядок не дорівнює "stop", перетворіть його в число і додайте до суми.
# 6. Виведіть повідомлення "Число прийнято" після кожного успішного введення числа.
# 7. Коли цикл завершиться, виведіть загальну суму введених чисел.

# Можна використати
# while True:
#   ...
#   break;

total_sum = 0 

while True:
  user_input = input("Введіть число ( або 'stop' для завершення): ")
  if user_input.lower() == 'stop':
   break
  try:
   number = float(user_input)
   total_sum += number
   print("Число прийнято")
  except ValueError:
   print("Введено некоректне число. Будь ласка, введіть число або 'stop'.")
   
print(f"Сума введених чисел: {total_sum}")

