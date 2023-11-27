# Тема: Підрахунок голосів на виборах
# Завдання: Створіть програму для підрахунку голосів на виборах.
# У вашій програмі є словник `candidate_votes`, де ключами є імена кандидатів,
# а значеннями - кількість голосів, які вони отримали. Користувач послідовно
# вводить імена кандидатів, на яких він хоче проголосувати.

# Після кожного вводу програма додає один голос до відповідного кандидата у словнику.
# Якщо введено ім'я, якого немає в списку, виведіть повідомлення про помилку. Програма завершується,
# коли користувач вводить "end", після чого потрібно вивести кінцевий підрахунок голосів для кожного кандидата.
#
# Очікуваний результат:
# Якщо у `candidate_votes` є кандидати {"Alice": 0, "Bob": 0, "Charlie": 0},
# і користувач вводить "Alice", "Bob", "Alice", "Dave", "end", програма виводить:
# 'Вибачте, кандидата Dave немає в списку.'
# {'Alice': 2, 'Bob': 1, 'Charlie': 0}

# Послідовність виконання:
# 1. Створіть словник `candidate_votes` з іменами кандидатів та їхніми початковими голосами.
# 2. Використовуйте цикл для читання вводу від користувача.
# 3. Перевірте, чи існує введене ім'я кандидата в словнику.
# 4. Якщо так, додайте один голос до відповідного кандидата.
# 5. Якщо ні, виведіть повідомлення про помилку.
# 6. Після отримання "end", виведіть кінцевий підрахунок голосів.
