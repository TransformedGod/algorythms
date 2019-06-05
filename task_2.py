# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

range1 = [random.randint(0, 20) for i in range(20)]
range2 =[]

for index, value in enumerate(range1):
    if value % 2 == 0:
        range2.append(index)

print(range1)
print(range2)