from collections import Counter

a = Counter()  # пустая коллекция
b = Counter('abrakadabra')  # коллекция на строке
c = Counter({'red': 2, 'blue': 4})  # коллекция на словаре
d = Counter(cats=4, dogs=5)  # коллекция основанная на ключевых элементах

print(a, b, c, d, sep='\n')
print(b['z'])  # выдаст 0 так как в b нет такого символа
b['z'] = 0  # добавили z в каунтер, но встречается z 0 раз
print(b)  # теперь будет показывать что z встречается 0 раз

print(list(b.elements()))  # элементс выводит только те значения, которые встречаются положительное количество раз

print(b.most_common(2))  # выводит задонное количество самых встречающихся значений

g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)
g.subtract(f)
print(g)
print('*' * 50)
print(set(g))  # перевод каунтер в множество
print(dict(g))  # перевод каунтер в словарь

g.clear()  # чистка каунтера
print(g)
print('*' * 50)
# Арифмметические и логические операции
x = Counter(a=3, b=1)
y = Counter(a=1, b=2)
print(x + y)
print(x - y)
print(x & y)
print(x | y)
print('*' * 50)
# Унарное сложение и вычитание
z = Counter(a=2, b=-4)
print(+z)
print(-z)