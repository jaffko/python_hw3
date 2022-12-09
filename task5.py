# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fibo_N = int(input('Введите натуральное N: '))
fibo_list = [1, 0, 1]
j = 1
for i in range(2, fibo_N + 1):
    fibo_list.append(fibo_list[j+i-1] + fibo_list[j+i-2])
    fibo_list.insert(0, fibo_list[j-i+2] - fibo_list[j-i+1])
    j += 1
print(fibo_list)
