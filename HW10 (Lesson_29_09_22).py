


# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).

file_domains = 'materials/domains.txt'
def read_domain_names (filename):
    file = open(filename, 'r')
    data = file.read()
    data = data.replace('.', '')
    return data
data = read_domain_names(file_domains)




# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

file_names = 'materials/names.txt'
def read_only_names (filename):
    file = open(filename, 'r')
    data = file.read()
    data = data.split('\t')[1::3]
    return data
data = read_only_names(file_names)




# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]