days_counter = 1
day_one = float(input('Введите результат первого дня в км '))

if day_one <= 0:
    print('Результат первого дня должен быть больше 0')
    exit()

day_n = float(input('Введите желаемый результат в км '))

if day_one >= day_n:
    print('Результат первого дня не может быть меньше или равен желаемому результату')
    exit()

while day_one < day_n:
    day_one *= 1.1
    days_counter += 1

    print(f'Желаемый результат будет достигнут на {days_counter} день')