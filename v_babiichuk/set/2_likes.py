# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.
def user_activity(liked_users, commented_users):

    users = set(liked_users) & set(commented_users)  #  intersection 

    return list(users)

liked_users = ["user_1", "user_2", "user_3", "user_4", "user_5"]

commented_users = ["user_2", "user_4", "user_6", "user_10", "user_3"]

result = user_activity(liked_users, commented_users)

print("Користувачі, які лайкнули і прокоментували пост одночасно:", result)