print('Ноль в качестве знака приведет к завершению программы')
while True:
    op = input('Введите знак (+, -, *, /): ')
    if op == '0':
        break
    elif op in ('+', '-', '*', '/'):
        x = float(input('Введите x: '))
        y = float(input('Введите y: '))
        if op == '+':
            print('%.2f' % (x + y))
        if op == '-':
            print('%.2f' % (x - y))
        if op == '*':
            print('%.2f' % (x * y))
        if op == '/':
            if y != 0:
                print('%.2f' % (x / y))
            else:
                print('Деление на ноль')
    else:
        print ('Неверный знак, попробуйте еще раз')