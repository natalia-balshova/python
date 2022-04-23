phrase = input('Введите фразу: ')
phrase_list = phrase.split()
print(phrase_list)
for ind, el in enumerate(phrase_list, 1):
    print(ind, el[0:10])
