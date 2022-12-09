# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint as rnd, random as random
size = int(input('Введите размерность массива: '))
my_list = [rnd(1, 10) + round(random(), 5) for _ in range(size-1)]
my_list.insert(rnd(0, size-1), rnd(1, 10))  # ну чтобы был один интеджер в листе :)))
print(my_list)
new_list = []
for item in my_list:
    if len(str(item).split('.')) > 1:
        new_list.append(str(item).split('.'))
print(new_list)
min_num = float(f'1.{new_list[0][1]}')
max_num = float(f'1.{new_list[1][1]}')
for item in new_list:
    if float(f'1.{item[1]}') > max_num:
        max_num = float(f'1.{item[1]}')
    if float(f'1.{item[1]}') < min_num:
        min_num = float(f'1.{item[1]}')
print(f'Разница между максимальным и минимальным равна {max_num} - {min_num} = {max_num - min_num}')
