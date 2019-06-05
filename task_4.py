# Определить, какое число в массиве встречается чаще всего.

import random

range1 = [random.randint(0, 20) for i in range(20)]
print(range1)

max_number = ""
max_count = 0

for i in set(range1):
    count = range1.count(i)
    if count > max_count:
        max_number = i
        max_count = count

print(f"Число {max_number} встречается {max_count} раз")
