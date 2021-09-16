num = int(input('Введите число: '))
summ = 0
num_nex = 1

for i in range(num):
    summ += num_nex
    num_nex /= -2
print(f'Сумма данной прогрессии: {summ}')
