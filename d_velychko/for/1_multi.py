# Тема: Використання циклів for і функції range

# Завдання: Написати програму, яка виводить таблицю множення для заданого користувачем числа.
# Число має бути зчитане з консолі. Таблиця множення повинна включати множення заданого числа на
# всі числа від 1 до 10.

# Очікуваний результат: Після введення числа, програма повинна вивести на екран десять рядків,
# де кожен рядок показує множення заданого числа на числа від 1 до 10.
# Наприклад, якщо користувач вводить число 5, програма має вивести рядки від "5 x 1 = 5" до "5 x 10 = 50".

# Послідовність виконання:
# 1. Запросити в користувача ввести число (назвемо його `multiplication_number`).
# 2. Використовуючи цикл `for` і функцію `range`, пройтися по всіх числах від 1 до 10.
# 3. У кожній ітерації циклу, виконати множення `multiplication_number` на поточне число з циклу.
# 4. Вивести результат кожної ітерації у форматі "{multiplication_number} x {ітератор} = {результат}".

multiplication_number = int(input("Введіть число для таблиці множення: "))

for i in range (1, 11):
   o = multiplication_number * i
   print(f"{multiplication_number} * {i} = {o}")