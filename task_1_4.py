import random
import cProfile

def summ_element(range1):
    minimum = min(range1)
    maximum = max(range1)

    min_index = range1.index(minimum)
    max_index = range1.index(maximum)

    if max_index < min_index:
        max_index, min_index = min_index, max_index

    summ = 0
    for i in range(min_index + 1, max_index):
        summ += range1[i]

    return summ

range1 = [random.randint(0, 100) for i in range(100000)]
summ_element(range1)


# 100 loops, best of 5: 3.9 usec per loop - 10
# 100 loops, best of 5: 18.6 usec per loop - 100
# 100 loops, best of 5: 108 usec per loop - 1000


# cProfile.run('summ_element(range1)') - 1000
#     8 function calls in 0.000 seconds
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 task_1.py:101(summ_element)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('summ_element(range1)') - 10000
#     8 function calls in 0.001 seconds
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.001    0.001 <string>:1(<module>)
# 1    0.000    0.000    0.001    0.001 task_1.py:101(summ_element)
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('summ_element(range1)') - 10000
#     8 function calls in 0.010 seconds
#
#     Ordered by: standard name
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#     1    0.000    0.000    0.010    0.010 task_1.py:101(summ_element)
#     1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#     1    0.005    0.005    0.005    0.005 {built-in method builtins.max}
#     1    0.005    0.005    0.005    0.005 {built-in method builtins.min}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# Вывод: линейная зависимость O(n), нет вложенных циклов. Функции min() и max() сработали быстрее циклов - самый
# быстрый вариант.