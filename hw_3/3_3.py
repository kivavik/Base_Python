def my_func(n_1, n_2, n_3):
    try:
        n_1, n_2, n_3 = float(n_1), float(n_2), float(n_3)
    except ValueError:
        return 'Ошибка данных'
    my_list = [n_1, n_2, n_3]
    my_list.remove(min(my_list))
    return sum(my_list)

n_1 = input('Введите первое число: ')
n_2 = input('Введите второе число: ')
n_3 = input('Введите третье число: ')

print(my_func(n_1, n_2, n_3))