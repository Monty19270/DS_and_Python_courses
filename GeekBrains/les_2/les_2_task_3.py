num = int(input('Введите число: '))
mun = 0

while num > 0:
    mun = mun * 10 + num % 10
    num //= 10
print(f'Обратное число: {mun}')