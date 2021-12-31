from itertools import zip_longest
import sys
users, hobby, users_hobby = sys.argv[1:]

users = open(users)
hobby = open(hobby)

users_text = users.readlines()
hobby_text = hobby.readlines()
result = ''
with open(users_hobby, 'w+') as f:
    for str_1, str_2 in zip_longest(users_text, hobby_text, fillvalue=None):
        if str_1 is not None:
            result += f'{str_1.strip()}: {str_2.strip() if str_2 is not None else str_2}' + '\n'
        else:
            exit(1)
    print(result)
    f.write(result)
users.close()
hobby.close()
