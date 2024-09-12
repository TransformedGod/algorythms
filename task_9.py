# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

max_num = 0
max_sum = 0
summ = 0
a = ""
while a != "0":
    a = input("Введите число, 0 - остановка: ")
    for i in a:
        summ += int(i)
        if summ > max_sum:
            max_sum = summ
            max_num = a
    summ = 0
print(f"Наибольшая сумма - {max_sum} от числа {max_num}")
