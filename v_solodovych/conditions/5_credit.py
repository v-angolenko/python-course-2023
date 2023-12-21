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

while True:
    getCreditHistory = input("\nЧи маєте ви хорошу кредитну історію (так або ні)?\n")
    if getCreditHistory.lower() == "так":
        hasGoodCreditHistory = True
        break
    elif getCreditHistory.lower() == "ні":
        hasGoodCreditHistory = False
        break
    else:
        print("Введене значення невірне!")

while True:
    try:
        monthlyIncome = float(input("\nВведіть місячний дохід:\n"))
        break
    except ValueError:
        None

while True:
    getLongTerm = input("\nЧи є ви постійним клієнтом банку? (так або ні)?\n")
    if getLongTerm.lower() == "так":
        isLongTermClient = True
        break
    elif getLongTerm.lower() == "ні":
        isLongTermClient = False
        break
    else:
        print("Введене значення невірне!")

if hasGoodCreditHistory == True and monthlyIncome > 20000 or isLongTermClient == True and monthlyIncome > 15000:
    print("\nВи маєте право на кредит\n")
else:
    print("\nВи не маєте права на кредит\n")

# Очікуваний результат:
# Програма запитує у користувача дані про кредитну історію,
# місячний дохід та чи є він постійним клієнтом банку,
# обробляє ці дані за допомогою операторів `and` та `or`
# і виводить повідомлення про можливість отримання кредиту.
