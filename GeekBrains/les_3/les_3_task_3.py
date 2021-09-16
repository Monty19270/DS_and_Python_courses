# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

volume = int(input('Введите количество элементов в массиве: '))

array = [random.randint(0, 100) for _ in range(volume)]
min_pos = 0
max_pos = 0
print(array)
for i in range(volume):
    if array[i] < array[min_pos]:
        min_pos = i
    elif array[i] > array[max_pos]:
        max_pos = i
array[max_pos], array[min_pos] = array[min_pos], array[max_pos]
print(array)
