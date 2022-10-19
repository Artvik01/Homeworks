import json
import random

path_current_data = 'current_data.json'
path_config = 'config.json'


def open_file_current_data():
    with open(path_current_data) as file:
        data = json.load(file)
        exchange_rate = data.get('course')
        uah = data.get('UAH')
        usd = data.get('USD')
        delta = data.get('delta')
    return exchange_rate, uah, usd, delta, data


data_from_current_data = open_file_current_data()
exchange_rate = data_from_current_data[0]
uah_available = data_from_current_data[1]
usd_available = data_from_current_data[2]
delta = data_from_current_data[3]
data = data_from_current_data[4]
print(data)

def write_file_current_data(uah_usd_available):
    with open(path_current_data, 'w') as file:
        json.dump(uah_usd_available, file)


def rate(exchange_rate):
    print(exchange_rate)


def available(usd_available, uah_available):
    print('USD', usd_available, 'UAH', uah_available)


def buy_xxx(amount, usd_available, uah_available, exchange_rate, data):
    amount_in_uah = float(amount) * exchange_rate
    if uah_available >= amount_in_uah:
        uah_available -= round(amount_in_uah, 2)
        usd_available += round(float(amount), 2)
        uah_usd_available_update = {"USD": usd_available,
                                    "UAH": uah_available}
        data.update(uah_usd_available_update)
        write_file_current_data(data)
    else:
        print('REQUIRED BALANCE UAH ', amount_in_uah, ' AVAILABLE ', uah_available)


def sell_xxx(amount, usd_available, uah_available, exchange_rate, data):
    amount_in_uah = float(amount) * exchange_rate
    if usd_available >= float(amount):
        uah_available += round(amount_in_uah, 2)
        usd_available -= round(float(amount), 2)
        uah_usd_available_update = {"USD": usd_available,
                                    "UAH": uah_available}
        data.update(uah_usd_available_update)
        write_file_current_data(data)
    else:
        print('REQUIRED BALANCE USD ', amount, ' AVAILABLE ', usd_available)


def buy_all(usd_available, uah_available, exchange_rate, data):
    value_usd = uah_available / exchange_rate
    uah_usd_available_update = {"USD": usd_available + round(value_usd, 2),
                                "UAH": uah_available - round(exchange_rate * value_usd, 2)}
    data.update(uah_usd_available_update)
    write_file_current_data(data)


def sell_all(usd_available, uah_available, exchange_rate, data):
    value_uah = usd_available * exchange_rate
    uah_usd_available_update = {"USD": 0,
                                "UAH": uah_available + round(value_uah, 2)}
    data.update(uah_usd_available_update)
    write_file_current_data(data)


def next_step(exchange_rate, delta, data):
    new_exchange_rate = round(random.triangular(exchange_rate - delta,
                                                exchange_rate + delta), 2)
    current_data_update = {"course": new_exchange_rate}
    data.update(current_data_update)
    write_file_current_data(data)


def restart():
    with open(path_config) as file_config:
        data_update = json.load(file_config)
    write_file_current_data(data_update)
