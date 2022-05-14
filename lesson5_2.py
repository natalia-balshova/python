with open('file_2.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    print(content)
    print(f"Количество строк: {len(content)}")
    i = 1
    for el in content:
        print(f" Список {i} состоит из {len(el.split())} строк")
        i += 1


