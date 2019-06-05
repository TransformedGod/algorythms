# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

range1 = [random.randint(0, 20) for i in range(20)]
print(range1)

minimum = range1[0]
for i in range1:
    if i < minimum:
        minimum = i

maximum = range1[0]
for i in range1:
    if i > maximum:
        maximum = i

min_index = range1.index(minimum)
max_index = range1.index(maximum)

range1[min_index], range1[max_index] = range1[max_index], range1[min_index]

print(range1)