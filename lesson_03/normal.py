# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    s = [0, 1, 1]
    i = 3
    while i <= m:
        s.append(s[i - 1] + s[i - 2])
        i += 1
    return s[n - 1:m]



print(fibonacci(10, 16))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list) - 1):
        for j in range(len(origin_list) - 1):
            if origin_list[j] < origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
lost = [99, 99, 99, 99, 4, 2, 10, -12, 101, 2.5, 20, 7, 3, -11, 4, 4, 4, 0]


def filt(arg, obj):
    print(obj)
    print('=' * 60)
    lst = []
    for i in obj:
        if i != arg:
            lst.append(i)
    print(lst)


filt(4, lost)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parall(a1, a2, a3, a4):

    if abs(int(a2[0]) - int(a1[0])) == abs(int(a3[0]) - int(a4[0])) and abs(int(a4[1]) - int(a1[1])) == abs(int(a3[1]) - int(a2[1])):
        return 'yes'
    else:
        return 'no'
print('Вводите координаты через пробел! ')
a1 = input('Введите координаты 1 точки: ')
a1 = a1.split()
a2 = input('Введите координаты 2 точки: ')
a2 = a2.split()
a3 = input('Введите координаты 3 точки: ')
a3 = a3.split()
a4 = input('Введите координаты 4 точки: ')
a4 = a4.split()
print(parall(a1, a2, a3, a4))
