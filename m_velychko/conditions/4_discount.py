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

isClubMember = input("Чи є ви членом нашого клубу? (Так/ні) ")

if isClubMember == 'так':
    isClubMember = True

elif isClubMember == 'ні':
    isClubMember = False

else:
    print('Неправильно введена відповідь. Будь ласка введіть "так" чи "ні".')
    exit()

purchaseAmount = int(input("Введіть вартість вашої покупки (гривні): "))

if isClubMember or purchaseAmount > 1000:
    print("Ви отримали знижки :)")
else:
    print("Ви не отримали знижки :(")