# Тема:
# Умовні оператори if-else в Python

# Завдання:
# Створіть скрипт Python, який аналізує значення двох змінних: `income` (дохід)
# та `expenses` (витрати). Скрипт повинен визначити, чи є бюджет позитивним (дохід більший за витрати),
# негативним (дохід менший за витрати), чи в балансі (дохід дорівнює витратам).
# На основі аналізу скрипт повинен вивести одне з наступних повідомлень:

# 1. "Ваш бюджет позитивний. Ви у плюсі на: [сума] грн."
# 2. "Ваш бюджет негативний. Ви у мінусі на: [сума] грн."
# 3. "Ваш бюджет збалансований. Ви на нулі."

# Для реалізації скористайтеся умовними операторами `if`, `elif` та `else`.
# Також не забудьте процес обчислення абсолютного значення різниці доходів та витрат, якщо бюджет негативний.

# Очікуваний результат:
# Програма приймає значення доходів та витрат від користувача, обробляє їх
# і виводить відповідне повідомлення згідно з логікою, описаною вище.

income = float(input("Введіть дохід: "))
expenses = float(input("Введіть витрати: "))

difference = income - expenses

if difference > 0:
    print("Ваш бюджет позитивний. Ви у плюсі на: ", difference ," грн.")

elif difference < 0:
    print("Ваш бюджет негативний. Ви у мінусі на: ", difference ," грн.")

else:
    print("Ваш бюджет збалансований. Ви на нулі.")