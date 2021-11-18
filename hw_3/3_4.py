def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >=0:
            return 'Ошибка данных: значения x должно быть действительным положительным числом, y должно быть целым отрицательным числом'
        else:
            result = 1
            i = 0
            while i < abs(y):
                result *= 1 / x
                i += 1
            return result
    except ValueError:
        return 'Ошибка ввода значений'

print(my_func(input('Введите значение x: '), input('Введите значение у: ')))