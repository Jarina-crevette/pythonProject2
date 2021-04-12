# лаб 1 задание 3 задача 8

import random

A = [34,65,4,37,51]

mas=(A)
maximum=mas[0]

for i in range (1,len(mas)):
    if mas[i]>maximum:
        maximum=mas[i]

print(maximum)


