# лаб 1 задание 2 задача 4

import random

n = int(input("Введите размер списка:\n"))
A = []

for i in range(n):
    a = random.randint(1, 9)
    A.append(a)

s = sum(A)

print("Элементы списка: ")
for i in range(n):
    print(A[i])


print("Остаточная стоимость оборудования через год- "+str(s)+"рублей")




