#1#
# Дано целое число (int). Определить сколько нулей в этом числе.

value = 30608030
number = '0'
sum1 = str(value).count(number)




#2#
# Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля.

value = 1002000
number = 0
for symbol in str(value):
    if int(symbol) == 0: number += 1
    else: number = 0




#3#
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = 'qwerty'
my_list_2 = 'asdfg'
my_result = my_list_1[1::2] + my_list_2[::2]




#4#
# Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1].

my_list = 'qwerty'
new_list = my_list[1:] + my_list[:1]




#5#
# Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop).

my_list = ['q', 'w', 'e', 'r', 't', 'y']
my_list = my_list + list(my_list.pop(0))




#6#
# Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit).

my_list = "43 34 56"
new_list = my_list.split()
sum1 = 0
for symbol in new_list:
    sum1 += int(symbol)




#7#
# Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin". (rfind, find - методы строк).

my_str = 'qwerty'
l_limit = 'w'
r_limit = 't'
symb1 = my_str.find(l_limit)
symb2 = my_str.rfind(r_limit)
sub_str = my_str[symb1 + 1:symb2]




#8#
# Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2).

my_str = "abcde"
result = []
for index, value in enumerate(my_str):
    if index % 2 == 0: part = my_str[index:index+2]
    if len(part) > 1: result.append(part)
    else: result.append(value+"_")




#9#
# Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
number = 0
for symbol in range(1, len(my_list) - 1):
    if my_list[symbol] > sum([my_list[symbol - 1], my_list[symbol + 1]]):
        number += 1




#10#
# Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list = [1, 2, 3, '11', '22', '33']
new_list = []
for symbol in my_list:
    if type(symbol) == str: new_list.append(symbol)




#11#
# Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

my_str = 'qwertyorty'
new_list = []
for symbol in my_str:
    amount = my_str.count(symbol)
    if amount == 1: new_list.append(symbol)




#12#
# Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str1 = 'qwertyi'
my_str2 = 'qwertyo'
my_list = []
for symb_1 in my_str1:
    for symb_2 in my_str2:
        if symb_1 == symb_2: my_list.append(symb_1)




#13#
# Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу.

my_str1 = 'aaaasdf1'
my_str2 = 'asdfff2'
my_list = []
new_str1 = ''
for symb_1 in my_str1:
    if my_str1.count(symb_1) == 1: new_str1 += symb_1
new_str2 = ''
for symb_2 in my_str2:
    if my_str2.count(symb_2) == 1: new_str2 += symb_2
for symb_1 in new_str1:
    for symb_2 in new_str2:
        if symb_1 == symb_2: my_list.append(symb_1)