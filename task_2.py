# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
#
# Примечание по профилированию кода: для получения достоверных результатов при замере времени необходимо исключить/заменить команды print и input в анализируемом коде.

import cProfile

def func(i, k):

    n = i * k
    range1 = [m for m in range(n)]
    range1[1] = 0

    for m in range(2, n):
        j = 0
        if range1[m] != 0 and j < n:
            j = m + m
            while j < n:
                range1[j] = 0
                j += m

    res = [m for m in range1 if m != 0]
    return res

def sieve(i):
    k = 10
    final = func(i, k)
    while i > len(final) - 1:
        k = k + 2
        final = func(i, k)

    return final[i - 1]

# i = int(input('Какое по счету натуральное число ищем: '))

sieve(i)

# при k = 2

# 100 loops, best of 5: 44.4 usec per loop - 10
# 100 loops, best of 5: 864 usec per loop - 100
# 100 loops, best of 5: 16.9 msec per loop - 1000


# cProfile.run('sieve(100)')
#     16 function calls in 0.001 seconds
#
#     Ordered by: standard name
#
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     3    0.001    0.000    0.001    0.000 task_2.py:22(func)
#     3    0.000    0.000    0.000    0.000 task_2.py:25(<listcomp>)
#     3    0.000    0.000    0.000    0.000 task_2.py:36(<listcomp>)
#     1    0.000    0.000    0.001    0.001 task_2.py:39(sieve)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('sieve(1000)')
#     20 function calls in 0.019 seconds
#
#     Ordered by: standard name
#
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#     4    0.016    0.004    0.018    0.005 task_2.py:22(func)
#     4    0.001    0.000    0.001    0.000 task_2.py:25(<listcomp>)
#     4    0.001    0.000    0.001    0.000 task_2.py:36(<listcomp>)
#     1    0.000    0.000    0.018    0.018 task_2.py:39(sieve)
#     1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#     4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('sieve(10000)')
#     28 function calls in 0.726 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.001    0.001    0.726    0.726 <string>:1(<module>)
# 6    0.596    0.099    0.720    0.120 task_2.py:22(func)
# 6    0.051    0.008    0.051    0.008 task_2.py:25(<listcomp>)
# 6    0.073    0.012    0.073    0.012 task_2.py:36(<listcomp>)
# 1    0.005    0.005    0.725    0.725 task_2.py:39(sieve)
# 1    0.000    0.000    0.726    0.726 {built-in method builtins.exec}
# 6    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ******************************************************************************************

# при k = 10
# 100 loops, best of 5: 66.4 usec per loop - 10
# 100 loops, best of 5: 776 usec per loop - 100
# 100 loops, best of 5: 8.49 msec per loop - 1000


# cProfile.run('sieve(100)')
#     8 function calls in 0.001 seconds
#
#     Ordered by: standard name
#
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     1    0.001    0.001    0.001    0.001 task_2.py:22(func)
#     1    0.000    0.000    0.000    0.000 task_2.py:25(<listcomp>)
#     1    0.000    0.000    0.000    0.000 task_2.py:36(<listcomp>)
#     1    0.000    0.000    0.001    0.001 task_2.py:39(sieve)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('sieve(1000)')
#     8 function calls in 0.010 seconds
#
#     Ordered by: standard name
#
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#     1    0.008    0.008    0.010    0.010 task_2.py:22(func)
#     1    0.001    0.001    0.001    0.001 task_2.py:25(<listcomp>)
#     1    0.001    0.001    0.001    0.001 task_2.py:36(<listcomp>)
#     1    0.000    0.000    0.010    0.010 task_2.py:39(sieve)
#     1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('sieve(10000)')
#     12 function calls in 0.361 seconds
#
#     Ordered by: standard name
#
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.001    0.001    0.361    0.361 <string>:1(<module>)
#     2    0.252    0.126    0.358    0.179 task_2.py:22(func)
#     2    0.091    0.045    0.091    0.045 task_2.py:25(<listcomp>)
#     2    0.016    0.008    0.016    0.008 task_2.py:36(<listcomp>)
#     1    0.002    0.002    0.360    0.360 task_2.py:39(sieve)
#     1    0.000    0.000    0.361    0.361 {built-in method builtins.exec}
#     2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод: похоже на O(n**2): вложенный цикл + генерация массива = O(n**2 + n), коэффициэнт отбрасывается.
# # Большее количество элементов массива, сгенеренное единоразово, работает быстрее, чем меньшее количество,
# сгенеренное за несколько вызовов функции (k = 2 медленнее, чем k = 10).