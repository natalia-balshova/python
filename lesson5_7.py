import json
from statistics import mean


income_list = []
firm_name_list = []
all_firms_income = []
with open('firma.txt', 'r', encoding='utf-8') as f:
    for firm in f:
        firm = firm.split()
        income = int(firm[2]) - int(firm[3])
        print(f'Прибыль {firm[1]} "{firm[0]}" составляет: {income}')
        firm_name_list.append(firm[0])
        all_firms_income.append(income)
        if income > 0:
            income_list.append(income)
    print(f'Средняя прибыль компаний с положительной прибылью cоставляет: {mean(income_list)}')
    my_zip = zip(firm_name_list, all_firms_income)
    my_dict = dict(my_zip)
    my_list = [my_dict, {'average profit': mean(income_list)}]
    print(my_list)
    with open('file.json', 'w') as my_f:
        json.dump(my_list, my_f)
