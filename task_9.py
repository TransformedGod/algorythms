# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print("Введите три разных числа: ")
a = float(input("Первое: "))
b = float(input("Второе: "))
c = float(input("Третье: "))

if b < a:
    if a < c:
        print(a)
    else:
        if b < c:
            print(c)
        else:
            print(b)
else:
    if b < c:
        print(b)
    else:
        if a < c:
            print(c)
        else:
            print(a)
