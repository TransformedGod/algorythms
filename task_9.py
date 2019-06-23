# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(4)]

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()

max_element = None

for j in range(len(matrix[0])):
    min_element = matrix[0][j]

    for i in range(len(matrix)):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]

    if max_element is None or max_element < min_element:
        max_element = min_element

print(max_element)