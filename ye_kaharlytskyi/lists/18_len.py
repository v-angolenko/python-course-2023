# ```
# Тема: Визначення кількості елементів у списку.

# Завдання: Ви працюєте в компанії, яка займається аналізом даних.
# Вам необхідно підготувати звіт про кількість замовлень за останній тиждень.
# У вас є список `orders`, який містить кількість замовлень для кожного дня: [12, 15, 7, 11, 14, 18, 9].
# Напишіть код, який визначає і виводить загальну кількість днів, за які було здійснено замовлення

# Очікуваний результат: Програма повинна вивести два рядки.
# Перший: "Загальна кількість днів з замовленнями: 7".
# ```

orders = [12, 15, 7, 11, 14, 18, 9]

days = len(orders)

print(f"Загальна кількість днів з замовленнями: {days}")