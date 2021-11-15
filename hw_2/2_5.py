my_list = [6, 5, 4, 4, 2, 2, 1, 1]
user_number = int(input("Введите новый элемент рейтинга: "))
i = 0
for n in my_list:
    if user_number <= n:
        i += 1

    elif user_number > n:
        break

my_list.insert(i, int(user_number))
print(my_list)