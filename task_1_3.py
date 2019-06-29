import random
import cProfile

def summ_element(range1):
    minimum = range1[0]
    maximum = range1[0]
    for i in range1:
        if i < minimum:
            minimum = i
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

range1 = [random.randint(0, 100) for i in range(100000)]
summ_element(range1)


# 100 loops, best of 5: 4.07 usec per loop - 10
# 100 loops, best of 5: 21.9 usec per loop - 100
# 100 loops, best of 5: 138 usec per loop - 1000


# cProfile.run('summ_element(range1)') - 1000
#     6 function calls in 0.000 seconds
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 task_1.py:101(summ_element)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('summ_element(range1)') - 10000
#     6 function calls in 0.001 seconds
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     1    0.001    0.001    0.001    0.001 task_1.py:101(summ_element)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('summ_element(range1)') - 100000
#     6 function calls in 0.013 seconds
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#     1    0.012    0.012    0.012    0.012 task_1.py:101(summ_element)
#     1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# Вывод: линейная зависимость O(n), нет вложенных циклов. Небольшое улучшение времени при объединении в один цикл.