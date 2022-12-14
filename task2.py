# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]]

from random import randint as rnd

my_list = [rnd(1, 10) for _ in range(int(input('Введите размерность массива: ')))]
result_list = []
print(my_list)
for i in range(len(my_list) // 2):
    result_list.append(my_list[i]*my_list[-i-1])
if len(my_list) % 2 != 0:
    result_list.append(my_list[len(my_list) % 2 + 1] ** 2)
print(result_list)
