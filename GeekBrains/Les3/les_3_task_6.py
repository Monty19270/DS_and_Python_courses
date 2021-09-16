# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

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
print(f'Позиция максимального элемента {max_pos}, позиция минимального - {min_pos}')
print(f'Их значения {array[max_pos]}, {array[min_pos]}')
max_pos, min_pos = min_pos, max_pos
summ = 0
for i in range(min_pos + 1, max_pos):
    summ += array[i]
print(f'Сумма элементов между ними равна: {summ}')
