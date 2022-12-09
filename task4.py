# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal_number = int(input('Введите десятичное число: '))
binary_number = ''
while decimal_number // 2 != 0:
    binary_number += str(decimal_number % 2)
    decimal_number //= 2
binary_number += str(decimal_number)
print(binary_number[::-1])
