# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

range1 = [i for i in range(2, 100)]
range2 = [i for i in range(2, 10)]
results = [0] * 8

for i in range1:
    for j in range2:
        if i % j == 0:
            results[j - 2] += 1

for i in range2:
    print(f"{range2[i - 2]} - {results[i - 2]}")