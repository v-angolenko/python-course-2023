# Тема: Відстеження кількості продуктів на складі
# Завдання:
# Створіть програму для управління запасами на складі.
# Програма має словник `product_stock`, де ключі - це назви продуктів,
# а значення - кількість наявних одиниць. Користувач вводить назву продукту та кількість,
# яку потрібно додати або відняти (наприклад, "+5" або "-3"). Програма має оновлювати кількість продуктів
# у словнику та виводити оновлену інформацію. Коли користувач вводить "end",
# програма повинна вивести кінцевий стан запасів у форматі словника.

# Очікуваний результат: Якщо у `product_stock` є продукти {"apples": 20, "bananas": 15},
# і користувач вводить "apples +5", "bananas -2", "end", програма виводить: {'apples': 25, 'bananas': 13}.

# Послідовність виконання:
# 1. Створіть словник `product_stock` з назвами продуктів та їхньою кількістю.
# 2. Використовуйте цикл для читання вводу від користувача.
# 3. Обробляйте введені дані, розбиваючи їх на назву продукту та зміну кількості.
# 4. Оновлюйте кількість продукту у словнику відповідно до введеної інформації.
# 5. Після отримання "end" виведіть кінцевий стан запасів.

# # Розділення введеного рядка на компоненти
# product_name, quantity_change = user_input.split() // Повертає кореж ('apples', '-2')

# # Перевірка, чи існує продукт у словнику
# if product_name in product_stock:
#     # Оновлення кількості продукту
#     ___ += int(quantity_change) # int('-3') => -3
# else:
#     print(f"Продукт {product_name} не знайдено.")

product_stock = {"apples": 20, "bananas": 15}
while True:
    print("Поточний стан запасів:", product_stock)
    user_input = input("Введіть назву продукту та кількість (+ або -): ")
    product_name, quantity_change = user_input.split()
    if product_name in product_stock:
        try:
            quantity_change = int(quantity_change)
            product_stock[product_name] += quantity_change
            print(f"Кількість продукту {product_name} оновлено.")
        except ValueError:
            print("Некоректна кількість. Будь ласка, введіть ціле число.")
    elif product_name.lower() == "end":
        print("Кінцевий стан запасів:", product_stock)
        break
    else:
        print(f"Продукт {product_name} не знайдено.")