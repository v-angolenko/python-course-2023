# Тема:
# Використання логічних операторів and у умовних конструкціях.

# Завдання:
# Створіть програму, яка запитує у користувача вік (age) та кількість відпрацьованих років (yearsOfWork).
# Програма має визначити, чи користувач може йти на пенсію, враховуючи наступні умови:
# - Якщо вік користувача 65 років або більше і кількість відпрацьованих років 20 або більше,
# то користувач може йти на пенсію;
# - Якщо вік користувача 60 років або більше і кількість відпрацьованих років 30 або більше,
# то користувач також може йти на пенсію;
# - В усіх інших випадках користувач не може йти на пенсію.

# Програма повинна вивести повідомлення "Ви можете йти на пенсію" або "Ви ще не можете йти на пенсію",
# залежно від введених даних.

# Очікуваний результат:
# Користувач вводить свій вік та кількість відпрацьованих років, а програма виводить,
# чи користувач може йти на пенсію згідно з вищевказаними критеріями.

age = int(input('Скільки вам років: '))
yearsOfWork = int(input('Скільки у відпрацьованих років: '))

if age > 65 and yearsOfWork > 20:
    print ('Дякую за співпрацю, можете іти на пенсію')

elif age > 60 and yearsOfWork > 30:
    print ('Дяку за співпрацю, можете іти на пенсію')

else:
    print('Ви неможете іти на пенсію')