with open('text_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя зарплата = {round(sum(employees_dict.values()) / len(employees_dict), 3)}')
    print(f'Cотрудники с окладом меньше 20 000 {[empl[0] for empl in employees_dict.items() if empl[1] < 20000]}')