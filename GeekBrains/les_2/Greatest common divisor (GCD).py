# coding=utf-8

# Простейший циклический алгоритм основанный на вычитании
def gcd_easy(m,n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


# Рекурсивный алгоритм основанный на нахождении остатка от деления
def gcd_rec(m, n):
    if n == 0:
        return m
    return gcd_rec(n, m % n)

# Циклический алгоритм основанный на нахождении остатка от деления
def gcd_cicle(m, n):
    while m != 0:
        m, n = n, m % n
    return m
