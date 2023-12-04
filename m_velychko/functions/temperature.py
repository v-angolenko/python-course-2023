# #### Тема:
# Функції та обробка числових даних

# #### Завдання:
# Створіть функцію `convert_temperature`, яка конвертує температуру з градусів Цельсія в градуси
# Фаренгейта та навпаки.
#
# Функція повинна приймати числове значення температури та одиниці виміру ('C' для Цельсія, 'F' для Фаренгейта)
# і повертати перетворене значення.

# #### Очікуваний результат:
# Функція конвертує температуру між градусами Цельсія та Фаренгейта.

# #### Послідовність виконання:
# 1. Визначте функцію `convert_temperature`, яка приймає два параметри:
# `temperature` (числове значення температури)
# та `unit` (одиниця виміру - 'C' або 'F').
# 2. Функція має перевіряти одиницю виміру та відповідно конвертувати температуру.
# 3. Формули конвертації:
#    - Цельсій у Фаренгейт: ( (°C × 9/5) + 32 )
#    - Фаренгейт у Цельсій: ( (°F − 32) × 5/9 )
# 4. Функція повинна повертати перетворене значення температури.
# 5. Перевірте роботу функції на різних вхідних даних.

def convert_temperature(temperature, unit):

    if unit.upper() == 'C':
        result = (temperature * 9/5) + 32

        return result
    
    elif unit.upper() == 'F':
        result = (temperature - 32) * 5/9

        return result
    
    else:
        print("Невірна одиниця виміру. Використовуйте 'C' або 'F'.")

celsius_temperature = 29.44

converted_to_fahrenheit = convert_temperature(celsius_temperature, 'C')

print(f"{celsius_temperature} градусів Цельсія = {converted_to_fahrenheit:.2f} градусів Фаренгейта")

fahrenheit_temperature = 85

converted_to_celsius = convert_temperature(fahrenheit_temperature, 'F')

print(f"{fahrenheit_temperature} градусів Фаренгейта = {converted_to_celsius:.2f} градусів Цельсія")
