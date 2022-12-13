#2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
#И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

import random

elements_a = int(input('Введите колличество А элементов: '))
elements_b = int(input('Введите колличество Б элементов: '))

table = []
avg_lines = []

for i in range(elements_b):
    table.append(list())
    sum = 0
    for j in range(elements_a):
        table[i].append(random.randint(0, 10))
        sum += table[i][j]
    avg_lines = (sum // elements_a)
    print(f'{table[i]} - {avg_lines}')

    