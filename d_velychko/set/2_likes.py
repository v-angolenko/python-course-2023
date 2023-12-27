# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.

def common_activity(liked_users, commented_users):
    # Використовуємо множини для знаходження унікальних користувачів
    liked_set = set(liked_users)
    commented_set = set(commented_users)

    # Знаходимо унікальних користувачів, які лайкнули і прокоментували пост одночасно
    common_users = liked_set.intersection(commented_set)

    return list(common_users)

# Приклад використання функції
liked_users = ['user1', 'user2', 'user3', 'user4', 'user5']
commented_users = ['user3', 'user4', 'user5', 'user6', 'user7']

result = common_activity(liked_users, commented_users)
print("Користувачі, які лайкнули і прокоментували пост одночасно:", result)
