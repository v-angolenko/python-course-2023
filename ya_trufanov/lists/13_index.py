# ```
# Тема: Використання методу list.index() для знаходження індексу
# елемента у списку та отримання даних через input.

# Завдання: Створіть програму, яка запитує у користувача ім'я,
# а потім шукає це ім'я у заздалегідь заданому списку імен `namesList`,
# який містить ['Anna', 'Oleksiy', 'Viktor', 'Olga', 'Ivan'].
# Якщо ім'я знаходиться у списку, програма повинна вивести повідомлення
# "Ім'я [введене ім'я] має індекс [індекс в списку] у списку namesList".
# Якщо ж ім'я відсутнє у списку, виведіть "Ім'я [введене ім'я] у списку namesList відсутнє".

# Очікуваний результат: Якщо користувач введе ім'я 'Olga', то програма має вивести:
# ```
# ```
# Ім'я Olga має індекс 3 у списку namesList
# ```
# ```
# Якщо користувач введе ім'я 'Petro', результатом має бути:
# ```
# ```
# Ім'я Petro у списку namesList відсутнє
# ```

namesList = ["Anna", "Oleksiy", "Viktor", "Olga", "Ivan"]

name = input("Введіть ім`я: ")

if name in namesList:
    print(f"Ім'я {name} має індекс {namesList.index(name)} у списку namesList")
else:
    print(f"Ім'я {name} у списку namesList відсутнє")
