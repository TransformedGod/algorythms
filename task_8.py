# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = []

for i in range(5):
    row = []
    summ = 0

    for j in range(4 - 1):
        num = int(input(f"Введите {j + 1}e число в стороке {i + 1}: "))
        summ += num
        row.append(num)

    row.append(summ)
    matrix.append(row)

for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()