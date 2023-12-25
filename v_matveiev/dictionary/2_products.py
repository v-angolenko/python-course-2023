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

def update_stock(stock, product, quantity_change):
    if product in stock:
        stock[product] += quantity_change
    else:
        print(f"Продукт {product} не знайдено.")

def print_stock(stock):
    print(f"Кінцевий стан запасів: {stock}")
product_stock = {"apples": 20, "bananas": 15}
while True:
    print("Для оновлення запасів введіть продукт та кількість (+ або -), або 'end' для завершення:")
    user_input = input()
    if user_input.lower() == "end":
        break
    input_components = user_input.split()
    if len(input_components) == 2 and input_components[1][0] in ['+', '-'] and input_components[1][1:].isdigit():
        product_name, quantity_change_str = input_components
        quantity_change = int(quantity_change_str)
        update_stock(product_stock, product_name, quantity_change)
        print_stock(product_stock)
    else:
        print("Неправильний формат введення. Спробуйте знову.")
