import random

N = int(input('Введите количество чисел в массиве: '))

array = [random.randint(0, N) for _ in range(N)]

print(array)

max_frq = 1
num = array[0]

for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]
if max_frq == 1:
    print('Все числа уникальны')
else:
    print(f'Число {num} встречается в массиве {max_frq} раз')
