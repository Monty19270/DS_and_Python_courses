# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

volume = int(input('Введите количество элементов в массиве: '))

array = [random.randint(-100, 100) for _ in range(volume)]
index = -1
print(array)
for i in range(volume):
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
print(f'Максимальный отрицательный элемент находится на позиции {index} и равен {array[index]}')