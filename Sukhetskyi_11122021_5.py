my_list = [24.13, 45.56, 80.0, 99.99, 0.12, 67.07, 23.25, 13.2, 60.9, 54.21]
my_list2 = []

# A
print('Задание A:')
for price in my_list:

    if my_list.index(price) == len(my_list) - 1:
        print(f'«{int(price)} руб {int(round(price * 100) % 100):02} коп».')
    else:
        print(f'«{int(price)} руб {int(round(price * 100) % 100):02} коп»', end=', ')
print('')

# B
print('Задание B:')
print(id(my_list), 'ID стартового списка')
my_list.sort()

for price in my_list:
    if my_list.index(price) == len(my_list) - 1:
        print(f'«{int(price)} руб {int(round(price * 100) % 100):02} коп».')
    else:
        print(f'«{int(price)} руб {int(round(price * 100) % 100):02} коп»', end=', ')
print(id(my_list), 'ID после отсортированного вывода по возрастанию')
print('')

# C
print('Задание С:')
print(id(my_list), 'ID стартового списка')
my_list2 = sorted(my_list)
my_list2.reverse()
print(my_list2)
print(id(my_list2), 'ID нового списка с ценами по убыванию')
print('')

# D
print('Задание D:')
print(my_list2[:5])
