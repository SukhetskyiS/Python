import os

folder = 'DLLs'  # Папка которую необходимо проверить
my_dict = {}
n = 0
bottom_line = 0

while 10 ** (n + 1) <= 100000:
    files = [item.name for item in os.scandir(folder) if bottom_line < item.stat().st_size <= 10 ** (n + 1)]
    my_dict.setdefault(10 ** (n + 1), len(files))
    n += 1
    bottom_line = 10 ** n
for key, val in my_dict.items():
    print(f'{key}: {val}')
