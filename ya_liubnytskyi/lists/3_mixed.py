# ```
# Тема: Створення списку з різними типами даних у Python.

# Завдання: Напишіть Python-скрипт, який створює список з назвою `mixedData`,
# що містить різні типи даних: ціле число, рядок, дробове число (з плаваючою точкою),
# і логічне значення (булеве). Наприклад, список може виглядати так: `[42, 'Python', 3.14, True]`.
# Після створення списку, програма повинна вивести кожен елемент списку в консоль на окремому рядку,
# використовуючи індексацію для доступу до елементів.

# Очікуваний результат:
# Після виконання скрипту в консолі мають бути виведені наступні рядки, кожен з нового рядка:
# ```
# ```
# 42
# Python
# 3.14
# True
# ```
mixedData = [42, 'Python', 3.14, True]
message = f'''
{mixedData[0]}
{mixedData[1]}
{mixedData[2]}
{mixedData[3]}
'''
print(message)