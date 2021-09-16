# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# версия python 3.83 win32
# версия windows 10 x64
import random
import sys

M = 40
N = 40
MIN_ITEM = 0
MAX_ITEM = 10

PRINT_MATRIX = False
SHOW_VARS = True
DETAIL = False

MATRIX = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)] for _ in range(M)]

if PRINT_MATRIX:
    for row in MATRIX:
        for element in row:
            print(f'{element:>4}', end='')
        print('')


def trace_func(frame, event, arg):
    if event == "return":
        global us_memory

        for key in frame.f_locals.keys():

            size = var_size(frame.f_locals[key])
            us_memory += size

            if SHOW_VARS:
                print(f'{key} {type(frame.f_locals[key])}: {size}')

            if DETAIL:
                print('')

    return trace_func


def var_size(x, level=0):
    res = sys.getsizeof(x)

    if DETAIL:
        print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}')

    if hasattr(x, '__iter__'):

        if hasattr(x, 'items'):
            for key, value in x.items():
                res += var_size(key, level + 1)
                res += var_size(value, level + 1)

        elif not isinstance(x, str):
            for item in x:
                res += var_size(item, level + 1)

    return res

# Кэшировние данных
def cache_optimized(matrix=MATRIX):

    min_array = [MAX_ITEM for _ in range(N)]

    for row in matrix:
        for i, el in enumerate(row):
            if min_array[i] > el:
                min_array[i] = el

    min_el = MIN_ITEM - 1

    for i in min_array:
        if i > min_el:
            min_el = i

    return min_el


# Дла функции cache_optimized:
# .0 <class 'range_iterator'>: 24
# _ <class 'int'>: 14
# matrix <class 'list'>: 30806
# min_array <class 'list'>: 694
# row <class 'list'>: 772
# i <class 'int'>: 12
# el <class 'int'>: 14
# min_el <class 'int'>: 14
# Суммарный объем памяти 32350


def column_move(matrix=MATRIX):
    res = float('-inf')
    columns = len(matrix[0])
    rows = len(matrix)

    for col in range(columns):

        min_el = matrix[0][col]
        for row in range(rows):

            if min_el > matrix[row][col]:
                min_el = matrix[row][col]

        if res < min_el:
            res = min_el

    return res


# Дла функции column_move:
# matrix <class 'list'>: 30806
# res <class 'int'>: 14
# columns <class 'int'>: 14
# rows <class 'int'>: 14
# col <class 'int'>: 14
# min_el <class 'int'>: 12
# row <class 'int'>: 14
# Суммарный объем памяти 30888


def with_transpose(matrix=MATRIX):
    res = float('-inf')
    tr_matrix = zip(*matrix)

    for tr_row in tr_matrix:

        min_el = tr_row[0]
        for el in tr_row:

            if el < min_el:
                min_el = el

        if res < min_el:
            res = min_el

    return res


# Дла функции with_transpose:
# matrix <class 'list'>: 30806
# res <class 'int'>: 14
# tr_matrix <class 'zip'>: 28
# tr_row <class 'tuple'>: 738
# min_el <class 'int'>: 12
# el <class 'int'>: 14
# Суммарный объем памяти 31612


funcs = [(cache_optimized, ()), (column_move, ()), (with_transpose, ())]

sys.settrace(trace_func)
for func, args in funcs:
    us_memory = 0
    print(f'Дла функции {func.__name__}:')
    sys.call_tracing(func, args)
    print(f'Суммарный объем памяти {us_memory}\n')
print(sys.platform)

# Минимальный объем памяти был выделен на выполнение функции column_move
# 30 888 байт, так как там используется только один список, в отличии от остальных функций.
