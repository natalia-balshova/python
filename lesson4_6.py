# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
# завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
# повторение элементов списка прекратится

import itertools

for n in itertools.count(3):
    if n == 10:
        break
    else:
        print(n)
my_list = ['hello', 100, 2.3, [1, 2]]
k = 0
for el in itertools.cycle(my_list):
    if k > 10:
        break
    print(el)
    k += 1

