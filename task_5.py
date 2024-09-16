# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

range1 = [random.randint(-10, 10) for i in range(20)]
print(range1)

range1_negative = []
for i in range1:
    if i < 0:
        range1_negative.append(i)

print(range1_negative)

max_number = range1_negative[0]
pos = 0

for i in range1_negative:
     if i > max_number:
         max_number = i
         pos = range1_negative.index(i)


print(f"Максимальное отрицательное значение: {max_number}, его позиция: {pos + 1}")
