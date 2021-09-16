#Решето Эратосфена

def eratosthenes(n):
    a = []
    b = []

    if n < 4:
        return

    for i in range(2, n + 1, 1):
        a.append(i)

    while a:
        for i in a[1:]:
            if i % a[0] == 0:
                b.append(i)
                a.remove(i)
        a = a[1:]

    for i in b:
        print(i, end=" ")


eratosthenes(15)

#Другой алгорим

def f_simpleInt():
    nn = 2
    while 1:
        nn += 1
        for i in range(2, nn):
            if nn % i == 0:
                break
            elif i == nn - 1:
                yield nn


genSimInt = f_simpleInt()

k = int(input('Введите число: '))
for i in range(k):
    si = next(genSimInt)

print(si)