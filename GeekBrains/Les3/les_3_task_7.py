import random

N = int(input('Введите количество чисел в массиве: '))

array = [random.randint(-N, N) for _ in range(N)]
if array[0] < array[1]:
    min_idx_1 = 1
    min_idx_2 = 0
else:
    min_idx_1 = 0
    min_idx_2 = 1

print(array)

for i in range (2, N):
    if array[i] < array[min_idx_1]:
        spam = min_idx_1
        min_idx_1 = i

        if array[spam] < array[min_idx_2]:
            min_idx_2 = spam
    elif array[i] < array[min_idx_2]:
        min_idx_2 = i

print(array[min_idx_2], array[min_idx_1])
