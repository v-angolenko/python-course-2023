# Тема: Змінні та базові типи даних

# Завдання:
# 1. Створіть змінну `book` та присвойте їй назву вашої улюбленої книги у вигляді рядка.
# 2. Створіть змінну `pages` та присвойте їй кількість сторінок цієї книги у вигляді цілого числа.
# 3. Створіть змінну `price` та присвойте їй вартість цієї книги у вигляді числа з плаваючою комою (наприклад, 199.99).
# 4. Виведіть на екран повідомлення у форматі: "Моя улюблена книга - [book].
# Вона має [pages] сторінок і коштує [price] гривень."

# Очікуваний результат:
# ```
# Моя улюблена книга - "1984". Вона має 328 сторінок і коштує 250.50 гривень.
# ```
# Примітка: Замініть "1984", "328" та "250.50" на власні значення, які ви ввели.

book = 'Мета. Процес безперервного вдосконалення'
pages = 448
price = 418.55

print(
    f'Моя улюблена книга - "{book}". Вона має {pages} сторінок і коштує {price:.2f} гривень.'
)
