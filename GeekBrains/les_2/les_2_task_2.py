num = int(input('Введите число: '))
even = odd = 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num //= 10
print(f'В данном числе {even} четных и {odd} нечетных цифр')