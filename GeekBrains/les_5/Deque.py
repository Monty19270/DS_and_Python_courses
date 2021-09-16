# Очередь

from collections import deque

# можно использовать все что можно запихнуть все что можно запихнуть в фор
a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
print(b, c, sep='\n')
print('*' * 50)
d = deque([i for i in range(5)], maxlen=7)
d.append(5)  # добаление справа
d.appendleft(6)  # добаление слува
print(d)
# можно добавлять несколькими элементами
d.extend([7, 8, 9])
d.extendleft([10, 11, 12]) # добавляет поочередно
print(d)

print('*' * 50)
f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')

print('*' * 50)
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2)) #количество вхожденяи элемента в очередь
print(g.index(3)) #позиция элемента в очереди
g.insert(2, 6) #добавление в середину очереди
print(g)

g.reverse() #переворот очереди
print(g)

g.rotate(3) #перемешие жлементов из правой в левую или из левой в правую часть(если n отрцательное) очереди
print(g)


