#n_1 - выработка в часах
#n_2 - ставка в час
#n_3 - премия

from sys import argv

print(argv)
name_of_script, n_1, n_2, n_3 = argv
salary = (int(n_1) * int(n_2)) + int(n_3)
print(f'В этом месяце вы отработали: {n_1} часов.\nПремия составила: {n_3} руб.\nЗаработная плата составила: {salary} руб.')