# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.

users = ["Ann", "Bob", "Tom", "Kate", "Alice"]
comments = ["Sam", "Charlie", "Sara"]

def activities(paramUsers: list[str], paramComments: list[str]) -> list[str]:
	lists = set(paramUsers) & set(paramComments)
	return list(lists)

print(activities(users, comments))