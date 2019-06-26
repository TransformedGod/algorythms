# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

def summ_element():
    range1 = [random.randint(0, 10) for i in range(10)]
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
    print(min_index, max_index)

    if max_index < min_index:
        max_index, min_index = min_index, max_index
    print(range1)

    summ = 0
    for i in range(min_index + 1, max_index):
        summ += range1[i]

    print(summ)

summ_element()