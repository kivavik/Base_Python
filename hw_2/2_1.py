print_list=[(1, 6), 10, 1.5, 'YOU', [1, 5, 6], True, 8.5,{112,'Beee',564},TypeError]

for i, item in enumerate(print_list, 1):
    print(f'{i}) {item}: {type(item)}')