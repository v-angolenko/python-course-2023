# ```
# Тема: Розрахунок загальної суми чеку з ресторану з урахуванням чаєвих.

# Завдання:
# Створіть програму, яка допомагає користувачу розрахувати загальну суму до оплати
# за обід у ресторані, включаючи чаєві. Програма має:
# 1. Запитати у користувача суму чеку від обіду.
# 2. Запитати у користувача відсоток чаєвих, який він бажає залишити.
# 3. Обчислити і вивести суму чаєвих.
# 4. Обчислити загальну суму до оплати, додавши чаєві до суми чеку.
# 5. Вивести результат з точністю до двох знаків після коми.

# Очікуваний результат:
# ```
# Введіть суму чеку: 750
# Введіть відсоток чаєвих: 10
# Сума чаєвих: 75.00 грн
# Загальна сума до оплати: 825.00 грн
# ```
bill_amount = float(input("Введіть суму чеку: "))
tip_percentage = float(input("Введіть відсоток чаєвих: "))
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
print(f"Сума чаєвих: {tip_amount:.2f} грн")
print(f"Загальна сума до оплати: {total_amount:.2f} грн")
