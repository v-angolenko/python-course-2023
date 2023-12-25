# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.


def get_activity_users(likes, comments):
    likes = set(likes)
    comments = set(comments)

    intersection = likes & comments
    return intersection


user_likes = ["user1", "user2", "user3", "user4", "user5", "user6"]
user_comments = ["user1", "user3", "user5", "user10"]

result = get_activity_users(user_likes, user_comments)
print(result)
