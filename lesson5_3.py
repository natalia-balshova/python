from statistics import mean

with open("salary.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    my_l = map(lambda my_str: my_str.split(), content)
    my_dict = dict(my_l)
    list_1 = []
    list_2 = []
    for key, value in my_dict.items():
        if float(value) < 20000:
            list_1.append(key)
        list_2.append(float(value))
    print(f"Фамилии сотрудников с окладом менее 20 тысяч: {', '.join(list_1)}")
    print(f"Средний оклад сотрудников составляет: {mean(list_2)}")
