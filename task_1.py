# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import cProfile
import random

def summ_element(n):
    range1 = [random.randint(0, 100) for i in range(n)]

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

    if max_index < min_index:
        max_index, min_index = min_index, max_index

    summ = 0
    for i in range(min_index + 1, max_index):
        summ += range1[i]

    return summ

summ_element(10)


# 100 loops, best of 5: 41.3 usec per loop - 10
# 100 loops, best of 5: 369 usec per loop - 100
# 100 loops, best of 5: 3.57 msec per loop - 1000


# cProfile.run('summ_element(100)')
#    525 function calls in 0.001 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:218(randint)
#       100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.001    0.001 task_1.py:14(summ_element)
#         1    0.000    0.000    0.001    0.001 task_1.py:15(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       118    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('summ_element(1000)')
#    5291 function calls in 0.006 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#      1000    0.002    0.000    0.004    0.000 random.py:174(randrange)
#      1000    0.001    0.000    0.005    0.000 random.py:218(randint)
#      1000    0.001    0.000    0.002    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.005    0.005 task_1.py:14(summ_element)
#         1    0.001    0.001    0.005    0.005 task_1.py:15(<listcomp>)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1284    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('summ_element(10000)')
#    52644 function calls in 0.056 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.056    0.056 <string>:1(<module>)
#     10000    0.019    0.000    0.040    0.000 random.py:174(randrange)
#     10000    0.008    0.000    0.048    0.000 random.py:218(randint)
#     10000    0.015    0.000    0.021    0.000 random.py:224(_randbelow)
#         1    0.001    0.001    0.056    0.056 task_1.py:14(summ_element)
#         1    0.007    0.007    0.054    0.054 task_1.py:15(<listcomp>)
#         1    0.000    0.000    0.056    0.056 {built-in method builtins.exec}
#     10000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12637    0.005    0.000    0.005    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# Вывод: больше всего времени приходится на саму генерацию рандомного массива, по работе алгоритма ничего сказать нельзя.
