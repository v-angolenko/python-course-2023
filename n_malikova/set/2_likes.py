# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.

def common_activity(likers, commenters):
    likers_set = set(likers)
    commenters_set = set(commenters)
    common_user = likers_set.intersection(commenters_set)
    return list(common_user)
likers_list = ["user1", "user2", "user3", "user4"]
commenters_list = ["user2", "user3", "user5", "user6"]
result = common_activity(likers_list, commenters_list)
print("Користувачі, які лайкнули і прокоментували одночасно: ", result)
