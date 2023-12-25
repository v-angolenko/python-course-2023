# ```
# Тема: Використання оператора del для видалення елементів списку.

# Завдання: У вас є список `mobileBrands`, що включає такі марки телефонів:
# ['Apple', 'Samsung', 'Xiaomi', 'Nokla', 'OnePlus'].
# Ви повинні видалити марку 'Nokla' з цього списку, використовуючи оператор `del`.
# Визначте індекс 'Nokla' в списку і видаліть цей елемент.
# Після виконання операції виведіть на екран оновлений список `mobileBrands`.

# Очікуваний результат: Після запуску програми, в консолі має бути виведений оновлений список `mobileBrands`
# без елемента 'Nokla':
# ```
# ```
# ['Apple', 'Samsung', 'Xiaomi', 'OnePlus']
# ```
mobileBrands = ['Apple', 'Samsung', 'Xiaomi', 'Nokla', 'OnePlus']
nokla_index = mobileBrands.index('Nokla')
del mobileBrands[nokla_index]
print(mobileBrands)
