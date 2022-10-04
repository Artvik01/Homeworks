import random
import string


# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

new_list = []
def uneven_inverse(my_list):
    for index, str_ in enumerate(my_list):
        if index % 2:
            new_list.append(str_[::-1])
        else:
            new_list.append(str_)
    return new_list




# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

def first_symbol_a(my_list):
    new_list = []
    for index in my_list:
         if "a" == index[0]:
            new_list.append(index)
    return new_list




# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

def any_symbol_a(my_list):
    new_list = []
    for index in my_list:
        if "a" in index:
            new_list.append(index)
    return new_list




# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

def only_str(my_list):
    result = []
    for index in my_list:
        if isinstance(index, str):
            result.append(index)
    return result




# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

def unique_list(my_str):
    my_list = []
    my_set = set(my_str)
    for symbol in my_set:
        amount = my_str.count(symbol)
        if amount == 1:
            my_list.append(symbol)
    return my_list




# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

def doubled_unique_list(my_str1, my_str2):
    my_list = list(set(my_str1) & set(my_str2))
    return my_list




# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

def unique_intersection(my_str1, my_str2):
    my_str1 = 'qwertyi'
    my_str2 = 'qwertyo'
    intersection = list(set(my_str1) & set(my_str2))
    unique_elements = []
    for element in intersection:
        if my_str1.count(element) == 1 and my_str2.count(element) == 1:
            unique_elements.append(element)
    return unique_elements




# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

def generate_rnd_str():
    rnd_lenths = random.randint(5, 7)
    rnd_string = random.choices(string.ascii_lowercase, k = rnd_lenths)
    rnd_string = ''.join(rnd_string)
    return rnd_string
def create_email(domains,names):
    rnd_domain = random.choice(domains)
    rnd_number = random.randint(100, 999)
    rnd_names = random.choice(names)
    rnd_string = generate_rnd_str()
    emails = str(rnd_names) + "." + str(rnd_number) + "@" + str(rnd_string) + "." + rnd_domain
    return emails
names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
email = create_email(domains, names)