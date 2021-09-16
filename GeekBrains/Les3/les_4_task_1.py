# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import cProfile
import timeit
import random


# volume = int(input('Введите количество элементов в массиве: '))


def replace():
    volume = 10000
    array = [random.randint(0, 100) for _ in range(volume)]
    min_pos = 0
    max_pos = 0
    for i in range(volume):
        if array[i] < array[min_pos]:
            min_pos = i
        elif array[i] > array[max_pos]:
            max_pos = i
    array[max_pos], array[min_pos] = array[min_pos], array[max_pos]
    return array


def replace2():
    volume = 10000
    array = [random.randint(0, 100) for _ in range(volume)]

    indexMin = array.index(min(array))
    indexMax = array.index(max(array))
    minMy = min(array)
    maxMy = max(array)

    array[indexMin] = maxMy
    array[indexMax] = minMy
    return array


def replace3():
    volume = 10000
    array = [random.randint(0, 100) for _ in range(volume)]
    array.sort()

    minMy = array[0]
    maxMy = array[-1]

    array[0] = maxMy
    array[-1] = minMy
    return array


# print(timeit.timeit(replace))
# print(timeit.timeit(replace2))
# print(timeit.timeit(replace3))
# cProfile.run('replace()')
# cProfile.run('replace2()')
# cProfile.run('replace3()')

# Применяя модуль Timeit находим время выполнения каждой функции при 14ти числах в массиве
# 15.2384947 sec - в первом варинте
# 14.566414000000002 sec - во втором варианте
# 13.182165599999998 sec - в третьем варианте
# Из этого можно сделать вывод, что быстрее всего работает функция под названием replace3

# В случае использования модуля cProfile время выполнения и количество вызовов внутри функций отличается не значительно
# 52597 function calls in 0.022 seconds
# 52643 function calls in 0.021 seconds
# 52608 function calls in 0.021 seconds
