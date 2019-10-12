from math import sqrt


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Side:
    def side(self, a, b):
        return round(sqrt(sum(tuple(map(lambda x1, x2: (x2 - x1) ** 2, a, b)))), 2)


class Tre(Side):
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    def sides(self):
        return {'AB': self.side(self.A, self.B),
                'BC': self.side(self.B, self.C),
                'CA': self.side(self.C, self.A),
                }

    def high(self):
        s = round(abs((self.B[1] - self.C[1]) * self.A[0] + (self.C[0] - self.B[0]) * self.A[1] + (
                self.B[0] * self.C[1] - self.C[0] * self.B[1])) / self.sides()['BC'], 2)
        z = round(abs((self.C[1] - self.A[1]) * self.B[0] + (self.A[0] - self.C[0]) * self.B[1] + (
                self.C[0] * self.A[1] - self.A[0] * self.C[1])) / self.sides()['CA'], 2)
        q = round(abs((self.A[1] - self.B[1]) * self.C[0] + (self.B[0] - self.A[0]) * self.C[1] + (
                self.A[0] * self.B[1] - self.B[0] * self.A[1])) / self.sides()['AB'], 2)
        # Это вычисление длины высоты через координаты ^_^
        return {'AH': s,
                'BH': z,
                'CH': q}

    def perim(self):
        return round(self.sides()['AB'] +
                     self.sides()['BC'] +
                     self.sides()['CA'], 2)

    def area(self):
        return round((lambda p, a, b, c: sqrt(p * (p - a) * (p - b) * (p - c)))
                     (self.perim() / 2,
                      self.sides()['AB'],
                      self.sides()['BC'],
                      self.sides()['CA']), 2)


A = tuple(input('Введите координаты A через пробел:').split())
B = tuple(input('Введите координаты B через пробел:').split())
C = tuple(input('Введите координаты C через пробел:').split())
l: list = sorted([A, B, C])
A = int(l[0][0]), int(l[0][1])
B = int(l[1][0]), int(l[1][1])
C = int(l[2][0]), int(l[2][1])
print('A{}, B{}, C{}'.format(A, B, C))
parameters = Tre(A, B, C)
print('Стороны: {}'.format(parameters.sides()))
print('Высоты: {}'.format(parameters.high()))
print('Преиметр: {}'.format(parameters.perim()))
print('Площадь: {}'.format(parameters.area()))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.side_a = sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        self.side_b = sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        self.side_c = sqrt((d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2)
        self.side_d = sqrt((a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2)

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c + self.side_d

    def square(self):
        return self.side_b + self.side_d / 4 * sqrt(4 * self.side_b - (self.side_b - self.side_d) ** 2)

    def isosceles(self):
        return True if self.side_a == self.side_c else False


coord_trap_a = (-1, 1)
coord_trap_b = (-2, -1)
coord_trap_c = (2, -1)
coord_trap_d = (1, 1)

trap = Trapeze(coord_trap_a, coord_trap_b, coord_trap_c, coord_trap_d)

print(trap.isosceles)
print(trap.square)
print(trap.perimeter)
# 2-ая задача легче из-за высот в первой, наверное все таки в первой надо было вычислять 1 длину высоты
