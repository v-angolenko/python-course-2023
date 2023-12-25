# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.
def find_common_users(liked_users, commented_users):
    liked_set = set(liked_users)
    commented_set = set(commented_users)

    common_users = liked_set.intersection(commented_set)

    return list(common_users)

liked_users = ['User1', 'User2', 'User3', 'User4']
commented_users = ['User2', 'User3', 'User5']

result = find_common_users(liked_users, commented_users)
print("Користувачі, які лайкнули і прокоментували пост одночасно:", result)