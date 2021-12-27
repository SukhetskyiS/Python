# Задача 1

def odd_nums(n):
    for number in range(1, n + 1, 2):
        yield number


print(*odd_nums(int(input('Диапазон развёрнутого генератора от 1 до ', ))))


# Задача 2

print(*(number for number in range(1, int(input('Диапазон короткого генератора от 1 до ', )) + 1, 2)))
