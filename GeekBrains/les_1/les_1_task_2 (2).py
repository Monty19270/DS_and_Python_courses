# По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки.

x_first = int(input('Введите x1: '))
y_first = int(input('Введите y1: '))
x_second = int(input('Введите x2: '))
y_second = int(input('Введите y2: '))

k = (y_first - y_second) / (x_first - x_second)
b = y_first - k * x_first
if b < 0:
    print("y = %.2f*x %.2f" % (k, b))
else:
    print("y = %.2f*x + %.2f" % (k, b))