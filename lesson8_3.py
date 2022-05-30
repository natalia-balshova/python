class CheckListError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        n = input('Введите число для списка: ')
        m = n.replace('.', '').replace('-', '')
        if m.isdigit() is False and n != 'stop':
            raise CheckListError('Это не число. Введите число.')
        elif n == 'stop':
            break
        else:
            my_list.append(n)
    except CheckListError as error:
        print(error)
        continue
print(my_list)
