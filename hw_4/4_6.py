from itertools import count, cycle

print('Нажмите "Enter" для генерации нового числа,для выхода нажмите "q"')
for i in count(int(input('Введите первое число: '))):
    print(i, end='')
    q = input()
    if q == 'q':
        break

print('Нажмите "Enter" для генерации повторения числа, для выхода нажмите "q"')
my_list = input('Введите список чисел через пробел: ').split()
my_iter = cycle(my_list)
q = None

while q !='q':
    print(next(my_iter), end='')
    q = input()
