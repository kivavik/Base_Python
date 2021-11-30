from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Зарплата: {time * rate + bonus}')
    except ValueError:
        print('Введены некорректные данные')

salary()