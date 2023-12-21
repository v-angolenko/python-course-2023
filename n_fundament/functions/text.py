# ### Завдання

# #### Тема:
# Функції та управління рядками

# #### Завдання:
# Напишіть функцію `analyze_text`, яка приймає текст, введений користувачем через `input()`,
# і аналізує його на предмет кількості слів та середньої довжини слова.

# #### Очікуваний результат:
# Функція повертає кількість слів у тексті та середню довжину слова.

# #### Послідовність виконання:
# 1. Визначте функцію `analyze_text`, яка приймає один параметр: `text` (текст для аналізу).
# 2. Функція має розділити текст на слова та підрахувати їх кількість.
# 3. Функція також має обчислити середню довжину слова в тексті.
# 4. Запросіть користувача ввести текст через `input()`.
# 5. Викликайте `analyze_text` з введеним текстом.
# 6. Виведіть результати аналізу: кількість слів та середня довжина слова.
# 7. Переконайтеся, що функція коректно обробляє різні вхідні дані.


def analyze_text(text: str) -> str:
    if text.isnumeric():
        return "Ви ввели число, а не текст."
    words = text.split()
    word_count = len(words)
    total_length = sum(len(word) for word in words)
    average_length = total_length / word_count if word_count > 0 else 0
    return f"Введений текст містить {word_count} слів, і середня довжина слова становить {average_length:.2f} символів."


input_text = input("Введіть текст: ")

print(analyze_text(input_text))
