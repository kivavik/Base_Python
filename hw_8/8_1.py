class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_data = []

        for i in day_month_year.split('-'):
            if i != '': my_data.append(i)

        return int(my_data[0]), int(my_data[1]), int(my_data[2])

    @staticmethod
    def valid(day_month_year):
        my_data = []

        for i in day_month_year.split('-'):

            if i != '': my_data.append(i)

        if 1 <= int(my_data[0]) <= 31:
            if 1 <= int(my_data[1]) <= 12:
                if 0 <= int(my_data[2]) <= 2021:
                    return f'Дата указана правильно!'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


my_day = input('Ввведите дату в формате dd-mm-yyyy: ')
today = Data(my_day)
print(today)
print(Data.extract(my_day))
print(Data.valid(my_day))
