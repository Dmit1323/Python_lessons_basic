# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class People:
    def __init__(self, name, patronymic, surname, birth_day, school, sex):
        self.name = name
        self.surname = surname
        self.birth_date = birth_day
        self.school = school
        self.sex = sex
        self.patronymic = patronymic

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


class Student(People):
    def __init__(self, name, patronymic, surname, birth_day, school, sex, class_room, parents):
        People.__init__(self, name, patronymic, surname, birth_day, school, sex)
        # Чтобы не обьявлять повторно, думаю это не будет ошибкой
        self.class_room = {'class_num': int(class_room.split()[0]),
                           'class_char': class_room.split()[1]}
        self.parents = {'mother': parents[0],
                        'father': parents[1]}

    def class_room(self):
        return "{} {}".format(self.class_room['class_num'], self.class_room['class_char'])

    def next_class(self):
        self.class_room['class_num'] += 1

    def get_fio(self):
        return str((self.surname, " ", self.name[0], ".", self.patronymic[0], "."))


class Teacher(People):
    def __init__(self, name, patronymic, surname, birth_day, school, sex, teach_classes, subject):
        People.__init__(self, name, patronymic, surname, birth_day, school, sex)
        self.teach_classes = teach_classes
        self.subject = subject


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

students = []
teachers = []


def get_clases():
    classes = set()
    for student in students:
        classes.add(student.class_room)
    return classes


def students_by_class(current_class):
    for student in students:
        if student.class_room == current_class:
            return student.get_fio()


def get_subjects(current_student):
    current_teachers = []
    current_subjects = []

    for student in students:

        if (student.surname, " ", student.name, " ", student.patronymic) == current_student:
            current_class = student.class_room

    try:
        for teacher in teachers:
            if current_class in teacher.teach_classes:
                current_teachers.append(teacher)
    except UnboundLocalError:

        return 'Ученик не найден'

    for current_teacher in current_teachers:
        current_subjects.append(current_teacher.subject)

    return current_subjects


def get_parents(current_student):
    for student in students:

        if (student.surname, " ", student.name, " ", student.patronymic) == current_student:
            return student.parents


def get_teachers_by_class(current_class):
    current_teachers = []
    for teacher in teachers:
        if current_class in teacher.teach_classes:
            current_teachers.append(teacher)

    return current_teachers
