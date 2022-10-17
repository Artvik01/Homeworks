import json
import random

filename = 'USD-UAH_Trader\\current_data.json'
filename_config = 'USD-UAH_Trader\\config.json'


def open_file_current_data():
    with open(filename) as file:
        data = json.load(file)
        exchange_rate = data.get('course')
        uah = data.get('UAH')
        usd = data.get('USD')
        delta = data.get('delta')
    return exchange_rate, uah, usd, delta


def write_file_current_data(data_update):
    with open(filename, 'w') as file:
        json.dump(data_update, file)
    pass


def rate():
    exchange_rate = open_file_current_data()[0]
    return exchange_rate


def available():
    uah = open_file_current_data()[1]
    usd = open_file_current_data()[2]
    return uah, usd


def buy_xxx(amount):
    amount_in_uah = amount * open_file_current_data()[0]
    if open_file_current_data()[1] >= amount_in_uah:
        open_file_current_data()[1] -= amount_in_uah
        open_file_current_data()[2] += amount
        data_update = {"USD": open_file_current_data()[2],
                       "UAH": open_file_current_data()[1]}
        write_file_current_data(data_update)
    else:
        print('REQUIRED BALANCE UAH ', amount_in_uah, ' AVAILABLE ', open_file_current_data()[1])
    pass


def sell_xxx(amount):
    amount_in_uah = amount * open_file_current_data()[0]
    if open_file_current_data()[2] >= amount:
        open_file_current_data()[1] += amount_in_uah
        open_file_current_data()[2] -= amount
        data_update = {"USD": open_file_current_data()[2],
                       "UAH": open_file_current_data()[1]}
        write_file_current_data(data_update)
    else:
        print('REQUIRED BALANCE USD ', amount, ' AVAILABLE ', open_file_current_data()[2])
    pass


def buy_all():
    value_usd = int(open_file_current_data()[1] / open_file_current_data()[0])
    data_update = {"USD": open_file_current_data()[2] + value_usd,
                   "UAH": open_file_current_data()[1] - value_usd * open_file_current_data()[0]}
    write_file_current_data(data_update)
    pass


def sell_all():
    value_uah = open_file_current_data()[2] * open_file_current_data()[0]
    data_update = {"USD": 0,
                   "UAH": open_file_current_data()[1] + value_uah}
    write_file_current_data(data_update)
    pass


def next_step():
    new_exchange_rate = round(random.triangular(open_file_current_data()[0] - open_file_current_data()[3],
                                                open_file_current_data()[0] + open_file_current_data()[3]), 2)
    data_update = {"course": new_exchange_rate}
    write_file_current_data(data_update)
    pass


def restart():
    with open(filename_config) as file_config:
        data_update = json.load(file_config)
    write_file_current_data(data_update)
    pass
