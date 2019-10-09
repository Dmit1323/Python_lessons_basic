# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

a = int(input('Введите номер действия: '))
if a == 1:
    try:
        for i in range(9):
            os.mkdir('dir_{}'.format(i+1))
    except Exception:
        print('Директории уже созданы.')
elif a == 2:
    try:
        for i in range(9):
            os.rmdir('dir_{}'.format(i+1))
    except Exception:
        print('Директорий не существует или они уже были удалены.')
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
if a == 3:
    print(os.listdir('.'))
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
if a == 4:
    name = os.path.realpath(__file__)
    new = name + '.dupl'
    if not(os.path.isfile(new)):
        shutil.copy(name, new)
    else:
        print('Копия уже сущетвует.')