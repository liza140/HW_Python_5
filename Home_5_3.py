# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютm. Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random

my_list = list(random.randint(1,10) for i in range(10))
print(my_list)

count = 0
for i in my_list:
    print(f"{i} встречается в списке {my_list.count(i)} раз(-а)")
    if my_list.count(i) > 1:
        count +=1

print("Количество совпадающих элементов: ", count)
print("Список уникальных элементов: ", list(set(my_list)))
