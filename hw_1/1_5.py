revenue = float(input('Введите выручку '))
cost = float(input('Введите издержки '))

profit = revenue - cost

if profit > 0:
    print(f'Прибыль {profit}')
    margin = (profit / revenue)
    print(f'Рентабельность {margin:.2f}')
    employee = int(input('Введите численность сотрудников '))
    pe = profit / employee
    print(f'Прибыль на сотрудника {pe:.2f}')
elif profit < 0:
    print(f'Убыток {profit}')
else:
    print ('Вы работает в ноль')