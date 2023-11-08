# Тема: Створення копії списку за допомогою методу list.copy() та його зворотнє
# сортування з використанням list.reverse().

# Завдання: Напишіть програму, яка спершу створює список з назвою `originalList`,
# що містить цілі числа від 1 до 5 включно.
# Далі, створіть копію цього списку і збережіть її у змінній `copiedList`
# за допомогою методу `copy()`. Використовуючи метод `reverse()`,
# виведіть на екран змінений список `copiedList`, який повинен бути відсортований у зворотному порядку.
# Після цього, програма має запитати у користувача через input "Введіть число для додавання
# у зворотньо відсортований список:", додайте введене число до `copiedList` і виведіть оновлений список на екран.

# Очікуваний результат: На початку програма виводить зворотньо відсортований список `[5, 4, 3, 2, 1]`.
# Після введення користувачем числа, наприклад 6, оновлений список повинен виглядати так: `[5, 4, 3, 2, 1, 6]`.

originalList = [1, 2, 3, 4, 5]
copiedList = originalList.copy()

copiedList.reverse()

print(originalList)

num = int(input('Введіть число для додавання у зворотньо відсортований список: '))
copiedList.append(num)

print(copiedList)
