# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

print("Введите три длины отрезков: ")
a = float(input("Длина первого отрезка: "))
b = float(input("Длина второго отрезка: "))
c = float(input("Длина третьего отрезка: "))

if a + b > c and a + c > b and b + c > a:
    if a == b:
        if b == c:
            print("Получился равносторонний треугольник")
        else:
            print("Получился равнобедренный треугольник")
    else:
        if b == c:
            print("Получился равнобедренный треугольник")
        else:
            if a == c:
                print("Получился равнобедренный треугольник")
            else:
                print("Получился разносторонний треугольник")
else:
    print("Такого треугольника не существует!")
