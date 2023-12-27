# 2. Напишіть функцію, яка аналізує активність користувачів
# деякої соціальної мережі відносно допису.
# Функція приймає список користувачів (наприклад, 10), які відмітили пост лайком та список користувачів,
# які прокоментували той же самий пост.
# Функція повертає імена унікальних користувачів, які лайкнули і прокоментували пост одночасно.

def both_checker(likers, commentators):
    likers_set = set(likers)
    commentators_set = set(commentators)
    both_set = likers_set.intersection(commentators_set)

    return both_set

likers_list = ['Grigirii', 'Inokentii', 'Amvrossii', 'Andrei', 'Ivan', 'Olena', 'Trevor', 'Yuri', 'Gregory', 'Michael']
commentators_list = ['Amvrossii', 'Abraham', 'Lincoln', 'Trevor', 'Paul', 'Patrick', 'Sara', 'Adam', 'Jena', 'Michael']
both_likers_and_commentators_list = list(both_checker(likers_list, commentators_list))

print(both_likers_and_commentators_list)