# Тема: Використання циклів for і функції range для аналізу даних

# Завдання: Написати програму, яка аналізує ряд чисел від 1 до 100 та визначає кількість чисел,
# які діляться націло на задане користувачем число. Це число має бути зчитане з консолі.

# Очікуваний результат: Програма зчитує число з консолі, а потім обчислює і
# виводить кількість чисел від 1 до 100, які діляться націло на введене число.
# Наприклад, якщо користувач вводить число 10, програма повинна вивести кількість чисел,
# кратних 10 в діапазоні від 1 до 100.

# Послідовність виконання:
# 1. Запросити в користувача ввести число (назвемо його `divisor`).
# 2. Ініціалізувати змінну для підрахунку (наприклад, `count`), встановивши її значення на 0.
# 3. Використовуючи цикл `for` і функцію `range`, пройтися по всіх числах від 1 до 100.
# 4. У кожній ітерації циклу перевірити, чи ділиться поточне число націло на `divisor` (за допомогою оператора `%`).
# 5. Якщо число ділиться, збільшити `count` на одиницю.
# 6. Після завершення циклу вивести кількість чисел, що відповідають умові (значення `count`).

divisor = int(input("Введіть число: "))

count = 0

for number in range(1, 101):
    if number % divisor == 0:
        count += 1

print(count)
