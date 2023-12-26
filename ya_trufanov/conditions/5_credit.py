# Тема:
# Комбінація логічних операторів `and` та `or` разом з функцією `input` для перевірки кредитної здатності.

# Завдання:
# Створіть програму для банку, яка дозволяє оцінити, чи має клієнт право на кредит.
#
# Клієнт може отримати кредит, якщо він має хорошу кредитну історію
# (змінна `hasGoodCreditHistory` зі значенням `True` або `False`),
# і його місячний дохід становить понад 20000 гривень (змінна `monthlyIncome`)
# або якщо він є постійним клієнтом банку (змінна `isLongTermClient` зі значенням `True` або `False`)
# та його місячний дохід становить понад 15000 гривень.
#
# Використовуйте комбінацію операторів `and` та `or` для визначення права на кредит та виведіть повідомлення
# "Ви маєте право на кредит" у випадку позитивної відповіді, та "Ви не маєте права на кредит"
# у випадку негативної.
#
# Дані про кредитну історію, місячний дохід та статус постійного клієнта повинні зчитуватися через `input`.

# Очікуваний результат:
# Програма запитує у користувача дані про кредитну історію,
# місячний дохід та чи є він постійним клієнтом банку,
# обробляє ці дані за допомогою операторів `and` та `or`
# і виводить повідомлення про можливість отримання кредиту.

monthlyIncome = float(input("Введіть свій місячний дохід: "))

if monthlyIncome < 15000:
    print("Ви не маєте право на кредит")
else:
    hasGoodCreditHistory = input("Ви маєте хорошу кредитну історію? (так/ні): ")
    isLongTermClient = input("Ви є постійним клієнтом банку? (так/ні): ")

    if (hasGoodCreditHistory == "так" and monthlyIncome > 20000) or (
        isLongTermClient == "так" and monthlyIncome > 15000
    ):
        print("Ви маєте право на кредит")
    else:
        print("Ви не маєте право на кредит")
