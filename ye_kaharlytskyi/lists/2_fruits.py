# ```
# Тема: Створення списку в Python.

# Завдання: Напишіть Python-скрипт, який створює список `fruits`, що містить назви фруктів.
# Потім додайте до цього списку ще один фрукт, назву якого програма повинна отримати
# від користувача через функцію `input()`. Виведіть оновлений список на екран.

# Очікуваний результат: Коли скрипт запущено, він спочатку створює список
# із заданими назвами фруктів, наприклад `['яблуко', 'банан', 'киві']`.
# Потім програма запитує у користувача ввести назву фрукта і додає цей фрукт до списку.
# Наприклад, якщо користувач введе "апельсин", оновлений список, який буде виведений,
# буде виглядати так: `['яблуко', 'банан', 'киві', 'апельсин']`.
# ```

fruits = ['Apple', 'Pear']

newFruit = input()

fruits.append(newFruit)

print(fruits)
