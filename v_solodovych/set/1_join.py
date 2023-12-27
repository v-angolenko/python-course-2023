# 1. Є дві множини A = {3, 5, 11, 7, 4, -3} та B = {11, 5, 8, 1, 10, 7}.
# Вивести в консоль елементи A, яких немає в B.
# Вивести в консоль елементи B, яких немає в A.
# Вивести в консоль спільні елементи A і B.
# Вивести в консоль об'єднання множин A і B.

A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}

C = A.difference(B)
D = B.difference(A)
E = A.intersection(B)
F = A.union(B)

print(C)
print(D)
print(E)
print(F)