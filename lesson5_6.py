with open('lessons.txt', 'r', encoding='utf-8') as f:
    lessons = []
    sums = []
    for my_list in f:
        my_list = my_list.split()
        new_list = []
        for el in my_list:
            el = el.replace(':', '')
            el = el.replace('(л)', '')
            el = el.replace('(пр)', '')
            el = el.replace('(лаб)', '')
            new_list.append(el)
            if el == '-':
                new_list.remove(el)
        lessons.append(new_list[0])
        my_sum = sum(list(map(lambda n: int(n), new_list[1:])))
        sums.append(my_sum)
    my_dict = dict(zip(lessons, sums))
    print(my_dict)
