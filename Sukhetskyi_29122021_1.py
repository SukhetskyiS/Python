import os

list_folder = ['settings', 'mainapp', 'adminapp', 'authapp']
for folder in list_folder:
    dir_path = os.path.join('my_project', folder)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
