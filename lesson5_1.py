f = open('file_1.txt', 'w', encoding='utf-8')
while True:
    n = input('Введите строку для файла (или нажмите Enter для завершения программы): ')
    content = f.writelines(f"{n}\n")
    if n == '':
        break
f.close()


