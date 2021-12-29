nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
flag = ["Англия", "Италия", "Испания", "Германия", "Франция"]
my_list = []
import random

def get_jokes(n):

    """Функция берет по одному случайному слову из каждого списка и добавляет в отдельный список.
    После чего удаляет использованные слова из начальных списков что бы они не повторялись при дальнейшем выводе шуток.
    После чего выводит сформированный список в зависимости от введенного n"""

    for i in range(n):
        random_nouns, random_adverbs, random_adjectives, random_flag = random.choice(nouns), random.choice(adverbs), random.choice(adjectives), random.choice(flag)
        my_list.append(f'{random_nouns} {random_adverbs} {random_adjectives} - это {random_flag}')
        nouns.pop(nouns.index(random_nouns))
        adverbs.pop(adverbs.index(random_adverbs))
        adjectives.pop(adjectives.index(random_adjectives))
        flag.pop(flag.index(random_flag))
    print(my_list)
get_jokes(int(input('Введите количество шуток: ', )))

"""Я наверное не понимаю задания. Если сделать аргументы именными(def get_jokes(n, *args):) то не будет работать перебор 
слов и выводить будет результат лишь по введенным аргументам. В общем сделал как понял"""
