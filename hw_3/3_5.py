def sum_num():
    s = 0
    while True:
        list_num = input('Введите числа через пробел или "Q" для выхода из программы: ').split()
        for num in list_num:
            if num.upper() == 'Q':
                return s
            else:
                try:
                    s += float(num)
                except ValueError:
                    print('Ошибка ввода данных. Введите числа через пробел или "Q" для выхода из программы: ')
        print(f'Сумма чисел равна: {s}')

print(f'Сумма чисел равна: {sum_num()}')