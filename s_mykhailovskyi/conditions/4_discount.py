# Тема:
# Використання оператора `or` у розгалуженні програми.

# Завдання:
# Уявіть, що ви розробляєте систему знижок для магазину.
# Клієнт отримує знижку, якщо він є членом клубу покупців ('isClubMember' == True)
# або його покупка перевищує 1000 гривень ('purchaseAmount' > 1000). Напишіть код,
# який запитує у користувача, чи є він членом клубу (ввести "так" або "ні")
# і вартість його покупки, а потім виводить "Ви отримали знижку!" або "Знижка не надається".

# Очікуваний результат:
# Користувач вводить свій статус члена клубу та суму покупки.
# На основі введеної інформації програма визначає, чи отримає клієнт знижку.

isClubMember = input("Чи є ви членом клубу? ")
purchaseAmount = int(input("Вартість вашої покупки: "))

if isClubMember == "так" or purchaseAmount > 1000:
    print("Ви отримуєте знижку")
else:
    print("Ви НЕ отримуєте знижку")