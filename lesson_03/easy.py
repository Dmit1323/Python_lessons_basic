# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = str(number)
    a = number.find('.') + 1
    ost = number[a:a + ndigits + 1]
    if int(ost[-1]) >= 5:
        ost = str(int(ost[:len(ost) - 1]) + 1)
        if len(ost) > ndigits:
            number = '{}.{}'.format(int(number[:a - 1]) + 1, ost[1:])
            return number
        else:
            number = '{}.{}'.format(number[:a - 1], ost)
            return number
    else:
        return number[:a + ndigits]





print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    n1 = ticket_number[:len(ticket_number) // 2]
    n2 = ticket_number[len(ticket_number) // 2:]
    s1 = 0
    s2 = 0
    for el in n1:
        s1 = s1 + int(el)
    for el in n2:
        s2 = s2 + int(el)
    if s1 == s2:
        return 'luck'
    else:
        return 'unluck'


print(lucky_ticket(123006))
print(lucky_ticket(123211))
print(lucky_ticket(436751))
