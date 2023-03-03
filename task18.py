
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках
# записаны N целых чисел Ai. Последняя строка содержит число X
import random
import math

n = int(input('введите количество элементов массива '))
min = int(input('введите мин элемент массива '))
max = int(input('введите макс элемент массива '))
x = int(input('введите число '))
array = [random.randint(min, max) for i in range(n)]
y = 0
y1 = 0
for i in range(len(array)):
    if abs(array[i] - x) != 0:
        if abs(array[i] - x) < abs(y - x): y = array[i]
        elif abs(array[i] - x) == abs(y - x) and array[i] != y: y1 = array[i]

print(array)
if y1 == 0: print('самое близкое число ', y)
else: print('самые близкие числа ', y, ' и', y1)
