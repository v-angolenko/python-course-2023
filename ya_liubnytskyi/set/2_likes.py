# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.


def user_activity(user_like, user_comment):
    users_list = set(user_like) & set(user_comment)
    return list(users_list)


user_like = ["user1", "user2", "user3", "user4",]
user_comment = ["user1","user3","user5","user6",]

result = user_activity(user_like, user_comment)
print(result)
