# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input("Введите трехзначное число: "))

c = n % 10
b = n // 10 %10
a = n // 100

print(a + b + c)
print(a * b * c)