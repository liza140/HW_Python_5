# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


import random

my_list = list(random.randint(1,10) for i in range(10))
print(my_list)

new_list = []
new_list.append(my_list[0])
index = 0
for i in range(len(my_list)):
    if my_list[i] > new_list[index]:
        new_list.append(my_list[i])
        index +=1
print(new_list)
