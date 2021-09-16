# coding=utf-8

# По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует,
# то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = int(input('Введите сторону a: '))
b = int(input('Введите сторону b: '))
c = int(input('Введите сторону c: '))

if a + b > c and a + c > b and b + c > a:
    if a == b or b == c or c == a:
        if a == b and b == c and c == a:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print("Треугольник не существует")