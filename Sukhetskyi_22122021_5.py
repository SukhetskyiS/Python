src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# В лоб
result = []
for number in src:
    if src.count(number) == 1:
        result.append(number)
print('result =', result)

# Оптимизированный
print('result =', [number for number in src if src.count(number) == 1])
