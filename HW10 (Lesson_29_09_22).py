# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).


file_domains = 'materials/domains.txt'
def read_domain_names (filename):
    with open(filename, 'r') as file:
        data = file.read()
        data = data.replace('.', '').split('\n')
        return data
data = read_domain_names(file_domains)




# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"


file_names = 'materials/names.txt'
def read_only_names (filename):
    result = []
    with open(filename, 'r') as file:
        file = file.read()
        file_data = file.splitlines()
        for line in file_data:
                data = line.split('\t')
                name = data[1]
                result.append(name)
    return result
result = read_only_names (file_names)




# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]


file_authors = 'materials/authors.txt'
def read_dates(filename):
    result = list()
    file = open(filename, 'r')
    file = file.read()
    file_read = file.splitlines()
    for symbol in file_read:
        if symbol != '':
            data = symbol.split('-')
            dates = data[0]
            if len(dates.split()) > 2:
                result.append({'date': dates})
    return result
result = read_dates(file_authors)