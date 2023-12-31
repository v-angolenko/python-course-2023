# Тема: Підрахунок щомісячного платежу за кредитом.

# Завдання:
# Напишіть програму на Python, яка дозволяє користувачеві розрахувати щомісячний
# платіж за кредитом. Програма повинна:
# 1. Запитати у користувача суму кредиту, яку він хоче взяти.
# 2. Запитати процентну ставку по кредиту за рік.
# 3. Запитати термін кредиту в роках.
# 4. Вирахувати та вивести щомісячний платіж за кредитом.

# Формула для обчислення щомісячного платежу (простий спосіб):
# Щомісячний платіж =
# (Сума кредиту + (Сума кредиту * (Процентна ставка / 100) * Термін кредиту)) / (Термін кредиту * 12)

# Очікуваний результат:
# ```
# Введіть суму кредиту: 50000
# Введіть процентну ставку по кредиту за рік: 7
# Введіть термін кредиту в роках: 5
# Ваш щомісячний платіж становитиме: 990 UAH
# ```

creditAmount = int(input("Введіть суму кредиту: "))
creditInterest = int(input("Введіть процентну ставку по кредиту за рік: "))
creditTerm = int(input("Введіть термін кредиту в роках: "))
monthlyPayment = (
    creditAmount + (creditAmount * (creditInterest / 100) * creditTerm)
) / (creditTerm * 12)
print(f"Ваш щомісячний платіж становитиме: {round(monthlyPayment, 2)} UAH")
