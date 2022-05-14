from random import randint

with open("file_4.txt", 'w+', encoding='utf-8') as f:
    f.write(' '.join([str(randint(1, 100)) for n in range(10)]))
    f.seek(0)
    content = f.read()
    content = content.split()
    my_sum = sum(list(map(lambda el: int(el), content)))
    print(f'Сумма элементов списка: {my_sum}')
