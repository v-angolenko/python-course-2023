# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.

def activity(liked_users, commented_users):

    users = set(liked_users).intersection(commented_users)

    return list(users)

liked_users = ["user1", "user2", "user3", "user4", "user5"]

commented_users = ["user2", "user4", "user6", "user7", "user8"]

result = activity(liked_users, commented_users)

print("Користувачі, які лайкнули і прокоментували пост одночасно:", result)