#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.

from collections import deque
ch={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
def sum(a, b):
    result = deque()
    tf = 0
    if len(b) > len(a):
        a, b = deque(b), deque(a)
    else:
        a, b = deque(a), deque(b)
    while a:
        if b:
            res = ch[a.pop()] + ch[b.pop()] + tf
        else:
            res = ch[a.pop()] + tf
        tf = 0
        if res < 16:
            result.appendleft(ch[res])
        else:
            result.appendleft(ch[res - 16])
            tf = 1
    if tf:
        result.appendleft('1')
    return list(result)
def pv(a, b):
    result = deque()
    spam = deque([deque() for _ in range(len(b))])
    a, b = a.copy(), deque(b)
    for i in range(len(b)):
        m = ch[b.pop()]
        for j in range(len(a) - 1, -1, -1):
            spam[i].appendleft(m * ch[a[j]])
        for _ in range(i):
            spam[i].append(0)
    tf = 0
    for _ in range(len(spam[-1])):
        res = tf
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res < 16:
            result.appendleft(ch[res])
        else:
            result.appendleft(ch[res % 16])
            tf = res // 16
    if tf:
            result.appendleft(ch[tf])
    return list(result)
a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())
print(a,'+',b,'=',sum(a, b))
print(a,'*',b,'=',pv(a, b))