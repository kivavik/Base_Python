def div(n_1, n_2):
    try:
        div_num = float(n_1) / float(n_2)
    except ValueError:
        return 'Ошибка данных'
    except ZeroDivisionError:
        return 'Деление на ноль'
    return div_num
print(div(input('Введите первое число: '), input('Введите второе число: ')))