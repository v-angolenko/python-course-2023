# 1. Є дві множини A = {3, 5, 11, 7, 4, -3} та B = {11, 5, 8, 1, 10, 7}.
# Вивести в консоль елементи A, яких немає в B.
# Вивести в консоль елементи B, яких немає в A.
# Вивести в консоль спільні елементи A і B.
# Вивести в консоль об'єднання множин A і B.
A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}
elements_only_in_A = A - B
print("Елементи A, яких немає в B:", elements_only_in_A)
elements_only_in_B = B - A
print("Елементи B, яких немає в A:", elements_only_in_B)
common_elements = A.intersection(B)
print("Спільні елементи A і B:", common_elements)
union_set = A.union(B)
print("Об'єднання множин A і B:", union_set)
