# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print("Введите две буквы латинского алфавита: ")
letter1 = input("Первая буква: ")
letter2 = input("Вторая буква: ")

position1 = ord(letter1) - 96
position2 = ord(letter2) - 96

if position1 > position2:
    range = position1 - position2
else:
    range = position2 - position1

print(f'Буква {letter1} стоит на {position1}м месте в алфавите, а буква {letter2} - на {position2}м, букв между ними: {range}.')