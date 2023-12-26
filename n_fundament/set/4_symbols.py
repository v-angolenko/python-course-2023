# 4. Напишіть функцію, яка приймає рядок символів (наприклад, "a14b6fh")
# і з використанням списків і множин визначає, чи всі символи в рядку унікальні.

omg_symbols = ["akjD9", "a14b6fh", "sk8DN2ask", "a14db6fha", "sk8DqwqN2ask", "sk8DN2e2ask"]

def unique_symbols(string: str) -> bool:
	return len(set(string)) == len(string)

for symbol in omg_symbols:
	print(unique_symbols(symbol))
