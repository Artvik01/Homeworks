import json
import re

filename = 'data.json'


def open_file_data(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


data = open_file_data(filename)


def sort_by_name(item):
    name = item['name']
    surname = name.split(' ')[-1]
    return surname


sorted_by_name_data = sorted(data, key=sort_by_name)


def sort_by_text_len(item):
    text = item['text']
    len_text = len(text.split(' '))
    return len_text


sorted_by_text_len_data = sorted(data, key=sort_by_text_len)


def sort_by_death_date(item):
    date = item['years']
    template = r"[0-9]"

    return template


sorted_by_death_date = sorted(data, key=sort_by_death_date)
print(sorted_by_death_date)
