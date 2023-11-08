# ```
# Тема: Перевірка наявності елемента в списку.

# Завдання: Ви створюєте систему управління складом і потребуєте перевірити наявність
# певного товару на складі. Ваш список товарів `inventory`
# істить такі елементи: "лопата", "граблі", "сапа", "коса". Напишіть код,
# який запитує у користувача назву товару (наприклад, "граблі") і перевіряє, чи є цей товар на складі.
# Якщо товар є в наявності, виведіть повідомлення "Товар [назва товару] є на складі",
# в іншому випадку - "Товар [назва товару] відсутній на складі".

# Очікуваний результат: Якщо користувач вводить "граблі", програма виводить:
# "Товар граблі є на складі". Якщо користувач вводить "мотика", програма виводить:
# "Товар мотика відсутній на складі".
# ```


instuments = ["лопата", "граблі", "сапа", "коса"]

name = input('Введіть назву товару: ')

if name in instuments:
    print(f"Товар {name} є на складі")
else:
    print(f"Товар {name} відсутній на складі")
