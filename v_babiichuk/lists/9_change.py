# Тема: Зміна значень елементів списку за індексом.

# Завдання: У вас є список з назвою `weekDays`,
# який містить дні тижня: ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П'ятниця', 'Субота', 'Неділя'].
# Ваше завдання - замінити 'Субота' та 'Неділя' на 'Субота - Вихідний' та 'Неділя - Вихідний' відповідно.
# Виконайте це, присвоївши нові значення елементам за відповідними індексами.
# Виведіть оновлений список `weekDays` на екран.

# Очікуваний результат: В консолі має бути виведений оновлений список `weekDays`,
# де два останніх дні містять уточнення про вихідний:
weekDays = ['Понеділок','Вівторок','Середа','Четвер','П`ятниця','Субота','Неділя']
weekDays[5] = 'Субота-Вихідний'
weekDays[6] = 'Неділя-Вихідний'
print(weekDays)