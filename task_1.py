# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    print("Введите два числа: ")
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    n = (input("Введите знак операции над ними (+, -, * или /), или 0 чтобы выйти: "))
    while n not in ("0", "+", "-", "*", "/"):
        n = input("Неправильно введен знак операции, введите еще раз: ")
    if n == "0":
        print("Программа завершилась")
        break
    else:
        if n == "+":
            res = a + b
        elif n == "-":
            res = a - b
        elif n == "*":
            res = a * b
        elif n == "/":
            if b == 0:
                print("Деление на ноль!")
                break
            else:
                res = a / b
        print("Результат:", res)