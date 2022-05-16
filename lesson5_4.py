with open("file_2.txt", "r", encoding='utf-8') as f:
    my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for content in f:
        content = content.split()
        content[0] = my_dict.get(content[0])
        content = ' '.join(content)
        with open("file_3.txt", "a", encoding='utf-8') as new_f:
            new_f.writelines(f"{content}\n")



