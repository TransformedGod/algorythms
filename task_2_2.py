# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
#
# sieve(2)
# 3
# prime(4)
# 7
# sieve(5)
# 11
# prime(1)
# 2

import cProfile

def func(i):
    plains = []
    q = i * 2
    while len(plains) < i - 1:
        q *= 2
        for m in range(2, q):
            mark = ""
            for j in range(2, i + 1):
                if m % j == 0 and m != j:
                    mark = False
            if mark != False and m not in plains:
                plains.append(m)
    return plains


def sieve(i):
    if i == 1:
        return 2
    number = func(i)[i - 1]
    return number

# i = int(input('Какое по счету натуральное число ищем: '))

# sieve(10)


# 10 loops, best of 5: 85.4 usec per loop - 10
# 10 loops, best of 5: 15.9 msec per loop - 100
# 10 loops, best of 5: 1.91 sec per loop - 1000


# cProfile.run('sieve(100)')
#     147 function calls in 0.018 seconds
#
#     Ordered by: standard name
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.018    0.018 <string>:1(<module>)
#     1    0.018    0.018    0.018    0.018 task_2_2.py:16(func)
#     1    0.000    0.000    0.018    0.018 task_2_2.py:31(sieve)
#     1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
#     3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     139    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('sieve(1000)')
#     1015 function calls in 2.126 seconds
#
#     Ordered by: standard name
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    2.126    2.126 <string>:1(<module>)
#     1    2.126    2.126    2.126    2.126 task_2_2.py:16(func)
#     1    0.000    0.000    2.126    2.126 task_2_2.py:31(sieve)
#     1    0.000    0.000    2.126    2.126 {built-in method builtins.exec}
#     3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1007    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('sieve(2000)')
#     3441 function calls in 19.437 seconds
#
#     Ordered by: standard name
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000   19.437   19.437 <string>:1(<module>)
#     1   19.435   19.435   19.437   19.437 task_2_2.py:16(func)
#     1    0.000    0.000   19.437   19.437 task_2_2.py:31(sieve)
#     1    0.000    0.000   19.437   19.437 {built-in method builtins.exec}
#     4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     3432    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод: очень тяжелый алгоритм. Для подсчета времени пришлось брать значения меньше, чем для других алгоритмов,
# иначе машина надолго зависала при подсчете. Сложность предположительно O(n**3) - два вложенных цикла, плюс долгая
# генерация массива.