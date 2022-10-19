from argparse import ArgumentParser
import utils as file

args = ArgumentParser()

args.add_argument('action', type=str)
args.add_argument('amount', nargs='?')

args = vars(args.parse_args())
action = args.get('action')
amount = args.get('amount')

if action == 'RATE':
    file.rate(file.exchange_rate)

elif action == 'AVAILABLE':
    file.available(file.usd_available, file.uah_available)

elif action == 'BUY':
    if amount == 'ALL':
        file.buy_all(file.usd_available, file.uah_available, file.exchange_rate, file.data)
    elif int(amount) > 0:
        file.buy_xxx(amount, file.usd_available, file.uah_available, file.exchange_rate, file.data)

elif action == 'SELL':
    if amount == 'ALL':
        file.sell_all(file.usd_available, file.uah_available, file.exchange_rate, file.data)
    elif int(amount) > 0:
        file.sell_xxx(amount, file.usd_available, file.uah_available, file.exchange_rate, file.ata)

elif action == 'NEXT':
    file.next_step(file.exchange_rate, file.delta, file.data)

elif action == 'RESTART':
    file.restart()
    