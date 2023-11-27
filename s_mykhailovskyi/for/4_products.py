# Тема: Цикли for, робота зі списками, використання input

# Завдання: Написати програму для ведення списку покупок.
#
# Програма повинна дозволяти користувачеві додавати назви продуктів до списку покупок,
# поки користувач не введе "готово". Після завершення вводу, програма повинна вивести повний список покупок.

# Очікуваний результат:
# Користувач вводить назви продуктів, один за одним.
# Кожен введений продукт додається до списку. Коли користувач вводить "готово",
# програма виводить на екран усі введені раніше продукти.

# Послідовність виконання:
# 1. Ініціалізувати пустий список (наприклад, `shopping_list`).
# 2. У безкінечному циклі (while), використовуючи `input()`, зчитувати від користувача назви продуктів.
# 3. Якщо користувач вводить "готово", завершити цикл.
# 4. Вивести весь список покупок (через for).

shopping_list = []

while True:
    goods = input("Введіть назву продукту: ")
    if goods == "готово":
        break
    else:
       shopping_list.append(goods) 

for good in shopping_list:
    print(good)