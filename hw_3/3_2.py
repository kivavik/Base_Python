def user_data(**kwargs):
    return ','.join(kwargs.values())

first_name = input('Введите имя: ')
last_name = input('Введите фамилия: ')
birthday = input('Введите год рождения: ')
city = input('Введите город: ')
email = input('Введите email: ')
phone = input('Введите номер телефона: ')

print(user_data(first_name=first_name.capitalize(), last_name=last_name.capitalize(), birthday=birthday, city=city.title(), email=email, phone=phone))
