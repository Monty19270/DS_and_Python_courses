import cProfile
import timeit


# n = int(input('До какого числа получать простые числа: '))

def sieve_er(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]  # генератор списка
    return (result)


def myfunction(n):
    b = []
    for i in range(2, n):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            b.append(i)
    return b

# cProfile.run("sieve_er(10000)")
# cProfile.run("myfunction(10000)")
#
# В случае с решетом Эратосфена функция выполняется за достаточно короткое время
# 6 function calls in 0.004 seconds
# Если рассмотреть функцию которуюб написал я, то получим
# 1233 function calls in 3.649 seconds
# 1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# заметное увеличение времени, а также количества итераций внутри функции
