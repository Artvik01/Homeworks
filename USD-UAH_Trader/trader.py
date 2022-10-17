from argparse import ArgumentParser
import utils as file

args = ArgumentParser()

args.add_argument('action', type=str)
args.add_argument('amount', nargs='?')

args = vars(args.parse_args())
action = args.get('action')
amount = args.get('amount')


if action == 'RATE':
    data = file.rate()
    print(data)

elif action == 'AVAILABLE':
    uah, usd = file.available()
    print('USD', usd, 'UAH', uah)

elif action == 'BUY':
    if amount == 'ALL':
        file.buy_all()
    elif int(amount) > 0:
        file.buy_xxx(amount)

elif action == 'SELL':
    if amount == 'ALL':
        file.sell_all()
    elif int(amount) > 0:
        file.sell_xxx(amount)

elif action == 'NEXT':
    file.next_step()

elif action == 'RESTART':
    file.restart()
    