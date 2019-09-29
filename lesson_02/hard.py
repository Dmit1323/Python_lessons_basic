
__author__ = 'Логинов Дмитрий Геннадьевич'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
k = ''
b = ''
i = 4
while equation[i] != 'x':
    k += equation[i]
    i += 1
k = float(k)
i += 1
while i < len(equation):
    if equation[i] != ' ':
        b += equation[i]
    i += 1
b = float(b)
print(k * x + b)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

date = input('Введите дату:')
if date[:2].isdigit() and date[3:5].isdigit() and date[6:].isdigit():
    day = int(date[:2])
    month = int(date[3:5])
    year = int(date[6:])
    if 0 < month < 13 and 0 < year < 10000:
        if month % 2 == 0:
            if not (0 < day < 32):
                print('Дата введена не корректно.')
            else:
                print('Дата введена корректно.')
        elif month % 2 != 0:
            if not (0 < day < 31):
                print('Дата введена не корректно.')
            else:
                print('Дата введена корректно.')
    else:
        print('Дата введена не корректно.')
else:
    print('Дата введена не корректно.')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
n = int(input('Введите номер комнаты: '))
i = 2 # Итерация квадрата башни
k = 1 # Комната
e = 1 # Этаж
m = 0 # Номер комнаты относительно левого края
while True:
    if n == 1:
        print('{}, {}'.format(k, e))
        break
    elif k < n:
        k = k + i * i
        e = e + i
        i += 1
        if k == n:
            print('{}, {}'.format(e, i - 1))
            break
    elif k > n:
        if k - (i - 1) >= n:
            k -= (i - 1)
            e -= 1
        elif k - (i - 1) < n:
            m = i - 1 - (k - n)
            print('{}, {}'.format(e, m))
            break
    elif k == n:
        if m > 0:
            print('{}, {}'.format(e, m))
        else:
            print('{}, {}'.format(e, i - 1))
        break
