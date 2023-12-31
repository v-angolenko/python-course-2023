# ```
# Тема: Вставка елементу в список за допомогою методу insert().

# Завдання: Ви маєте список з назвою `favoriteFruits`, який містить такі фрукти: 'яблуко', 'банан', 'киві'.
# Використовуючи метод `insert()`, додайте 'полуниця' так, щоб вона була другим елементом
# у списку (між 'яблуко' та 'банан').
# Після додавання елементу виведіть весь список `favoriteFruits` на екран.

favoriteFruits = ["яблуко", "банан", "киві"]
favoriteFruits.insert(1, "полуниця")

print(favoriteFruits)

# Очікуваний результат: Виведення на екран оновленого списку `favoriteFruits`, де 'полуниця'
# з'являється на другій позиції:
# ```
# ```
# ['яблуко', 'полуниця', 'банан', 'киві']
# ```
