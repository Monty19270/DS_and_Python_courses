import random

size = 6
array = [random.randint(1, 100) for _ in range(size)]
print(f'Дан массив : {array}, в котором два наименьших элемента: ')

pos_min = 0

for j in range(size):
    if array[j] < array[pos_min]:
        pos_min = j

print(f'- первый наименьший элемент: {array[pos_min]}')

array.remove(array[pos_min])

for j in range(size - 1):
    if array[j] < array[pos_min]:
        pos_min = j

print(f'- второй наименьший элемент: {array[pos_min]}')