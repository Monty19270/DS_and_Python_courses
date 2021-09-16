# coding=utf-8

# Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

string = 'Среднее число: {}'
if c < a < b or b < a < c:
    print(string.format(a))
elif c < b < a or a < b < c:
    print(string.format(b))
else:
    print(string.format(c))
