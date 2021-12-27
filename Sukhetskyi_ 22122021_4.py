src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print('result =', [number for i, number in enumerate(src) if number > src[i - 1] and i != 0])
