my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for element_of_list in my_list: # перебираем элементы списка по очереди
    if element_of_list.isdigit() == True: # проверяем является ли элемент числом
        digit_index = my_list.index(element_of_list) # находим индекс числового элемента в списке
        my_list.pop(digit_index) # удаляем найденный числовой элемент
        element_of_list = f'{int(element_of_list):02}' # переводим в int и дополняем до двух целочисленных разрядов
        element_of_list = '"' + element_of_list + '"' # берем в кавычки
        my_list = my_list[:digit_index] + [element_of_list] + my_list[digit_index:] # добавляем полученное назад на место удаленного элемента

    if element_of_list[1:].isdigit() == True: # проверяем является ли элемент числом после первого знака, так как это может быть число со знаком вначале
        digit_index = my_list.index(element_of_list) # находим индекс числового элемента в списке
        my_list.pop(digit_index) # удаляем найденный числовой элемент
        element_of_list =  element_of_list[0] + f'{int(element_of_list[1:]):02}' # соединяем первый знак элемента с числом (дополненным до двух целочисленных разрядов)
        element_of_list = '"' + element_of_list + '"' # берем в кавычки
        my_list = my_list[:digit_index] + [element_of_list] + my_list[digit_index:] # добавляем полученное назад на место удаленного элемента

print(' '.join(my_list)) # выводим полученный список в виде строки через пробел



