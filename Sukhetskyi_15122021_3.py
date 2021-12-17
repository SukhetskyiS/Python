my_list = ["Иван", "Мария", "Петр", "Илья"]
my_list_different = []
my_list_repeat = []

def thesaurus(args):
    my_dict = {}
    for name in args:
        kei = name[0]

        if kei not in my_dict:
            my_list_different = [name]
            my_dict[kei] = my_list_different
        else:
            my_list_repeat = [name]
            my_dict[kei].extend(my_list_repeat)
    for key, value in my_dict.items():
        print(f'{key} : {value}')

thesaurus(my_list)
