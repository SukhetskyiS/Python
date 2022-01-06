import os
import shutil

final_dir = r'D:\hw\L7\my_project\templates'

for r, d, f in os.walk('my_project'):
    if d == ['templates']:
        shutil.copytree(os.path.join(r, ''.join(d)), final_dir, dirs_exist_ok=True)
