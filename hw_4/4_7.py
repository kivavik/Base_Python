from itertools import count
from math import factorial

def fact_gen():
    for el in count(1):
        yield factorial(el)

gen = fact_gen()
print('Функция получения факториала числа от 1 до "n"')
x = 1
y = int(input('Введите последнее число "n": '))

for i in gen:
    if x > y:
        break
    else:
        print(f'{x}! = {i}')
        x += 1