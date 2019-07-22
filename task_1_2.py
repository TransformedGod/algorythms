import random
import cProfile

def summ_element(range1):
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

range1 = [random.randint(0, 100) for i in range(100000)]
summ_element(range1)

# 100 loops, best of 5: 4.07 usec per loop - 10
# 100 loops, best of 5: 23.3 usec per loop - 100
# 100 loops, best of 5: 169 usec per loop - 1000


# cProfile.run('summ_element(range1)') - 1000
#     6 function calls in 0.000 seconds
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 task_1.py:102(summ_element)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('summ_element(range1)') - 10000
#     6 function calls in 0.002 seconds
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#     1    0.002    0.002    0.002    0.002 task_1.py:102(summ_element)
#     1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('summ_element(range1)') - 100000
#     6 function calls in 0.015 seconds
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#     1    0.015    0.015    0.015    0.015 task_1.py:102(summ_element)
#     1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# Вывод: линейная зависимость O(n).