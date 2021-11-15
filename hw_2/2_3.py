my_month = input('Введите номер месяца от 1 до 12: ')
if 0 < int(my_month) <= 12:

     season = ['зима', 'весна', 'лето', 'осень']
     season_dic = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
     print(f'Сезон: {season[int(my_month)//3]}')
     print(f'Сезон (словарь): {season_dic[int(my_month)//3]}')

else:
    print('Ошибка')