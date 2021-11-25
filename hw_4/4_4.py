from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
print(f'Начальный список: {my_list}')
uniq_list = [el for el in my_list if my_list.count(el) ==1]
print(f'Уникальный список: {uniq_list}')