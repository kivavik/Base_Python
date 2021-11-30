my_list = input('Введите числа через пробел: ').split()

new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]

print(new_list)
