# ```
# Тема: Додавання елементів до списку.

# Завдання: Створіть список з назвою `gadgets`, який містить наступні рядки: 'смартфон', 'ноутбук'.
# Додайте до цього списку ще два гаджети — 'планшет' та 'смарт-годинник', використовуючи метод `append()`.
# Після додавання виведіть весь список на екран.

# Очікуваний результат: Виведений список має містити чотири елементи. Приклад виведення у консоль:
# ```
# ```
# ['смартфон', 'ноутбук', 'планшет', 'смарт-годинник']
# ```

devices = ['смартфон', 'ноутбук']

devices.append('планшет')
devices.append('смарт-годинник')

print(devices)