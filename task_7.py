# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

range1 = [random.randint(0, 10) for i in range(10)]
range2 = range1.copy()
print(range1)

min1 = range1[0]
for i in range1:
    if i < min1:
        min1 = i

range2.remove(min1)

min2 = range2[0]
for i in range2:
    if i < min2:
        min2 = i

print(min1, min2)
