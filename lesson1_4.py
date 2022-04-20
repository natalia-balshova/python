number = int(input('Введите целое положительное число '))
max_num = 0
while number > 0:
    last_num = number % 10
    if last_num > max_num:
       max_num = last_num
    number = number // 10
print('Максимальная цифра в числе: ', max_num)