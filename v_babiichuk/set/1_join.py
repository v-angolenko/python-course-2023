# 1. Є дві множини A = {3, 5, 11, 7, 4, -3} та B = {11, 5, 8, 1, 10, 7}.
# Вивести в консоль елементи A, яких немає в B.
# Вивести в консоль елементи B, яких немає в A.
# Вивести в консоль спільні елементи A і B.
# Вивести в консоль об'єднання множин A і B.
set_A = {3, 5, 11, 7, 4, -3}
set_B = {11, 5, 8, 1, 10, 7}
set_C = set_A - set_B 
set_D = set_B - set_A
set_E = set_A & set_B 
set_F = set_A | set_B 

print("Елементи A, яких немає в B:", set_A - set_B)  # або set_A.difference(set_B)
print("Елементи B, яких немає в A:", set_B - set_A)  # або set_B.difference(set_A)
print("Cпільні елементи A і B:", set_A & set_B)  # або set_A.intersection(set_B)
print("Об'єднання множин A і B:", set_A | set_B) # або set_A.union(set_B)