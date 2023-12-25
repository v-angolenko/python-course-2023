# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.
def find_common_users(likers, commenters):
    common_users = []
    likers_set = set(likers)
    commenters_set = set(commenters)
    for user in likers_set:
        if user in commenters_set:
            common_users.append(user)

    return common_users
likers_input = input("Введіть користувачів, які лайкнули (через кому): ")
commenters_input = input("Введіть користувачів, які прокоментували (через кому): ")
likers_list = likers_input.split(", ")
commenters_list = commenters_input.split(", ")
result = find_common_users(likers_list, commenters_list)
print("Користувачі, які лайкнули і прокоментували пост одночасно:", result)
