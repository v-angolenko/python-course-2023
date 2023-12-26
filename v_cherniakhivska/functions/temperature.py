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
    if unit == 'C':
        result = (temperature * 9/5) + 32
        return result
    elif unit == 'F':
        result = (temperature - 32) * 5/9
        return result
    else:
        return "Невірна одиниця виміру. Введіть 'C' або 'F'."

temperature_celsius = float(input("Введіть температуру в градусах Цельсія: "))
converted_temperature_fahrenheit = convert_temperature(temperature_celsius, 'C')
print(f"Температура в градусах Фаренгейта: {converted_temperature_fahrenheit:.2f}°F")

temperature_fahrenheit = float(input("Введіть температуру в градусах Фаренгейта: "))
converted_temperature_celsius = convert_temperature(temperature_fahrenheit, 'F')
print(f"Температура в градусах Цельсія: {converted_temperature_celsius:.2f}°C")