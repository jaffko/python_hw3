# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rnd
rnd_list = [rnd(0, 100) for _ in range(int(input('Введите размерность массива: ')))]
print(rnd_list)
odd_sum = 0
for i in range(1, len(rnd_list), 2):
    odd_sum += rnd_list[i]
print(f'Сумма на нечетных индексах = {odd_sum}')
