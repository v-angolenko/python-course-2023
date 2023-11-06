# Тема: Розрахунок вартості покупки зі знижкою.

# Завдання:
# Створіть програму, яка запитує в користувача ціну товару без знижки та
# розмір знижки (у відсотках). Програма має вирахувати та вивести на екран
# суму знижки та кінцеву ціну товару з урахуванням знижки.

# Очікуваний результат:
# ```
# Введіть ціну товару без знижки: 500
# Введіть розмір знижки (у %): 20

# Сума знижки: 100 грн.
# Ціна товару зі знижкою: 400 грн.
# ```

original_price = float(input("Введіть ціну товару без знижки: "))
discount_percentage = float(input("Введіть розмір знижки (у %): "))

discount_amount = (discount_percentage / 100) * original_price
final_price = original_price - discount_amount

print(f"Сума знижки: {discount_amount} грн.")
print(f"Ціна товару зі знижкою: {final_price} грн.")