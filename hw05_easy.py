# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), f'dir_{i}')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
for i in range(1,10):
    dir_path = os.path.join(os.getcwd(), f'dir_{i}')
    os.rmdir(dir_path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print(os.listdir(path=os.getcwd()))
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
shutil.copyfile(os.path.realpath(__file__), os.path.join(os.getcwd(), 'copy.py'))