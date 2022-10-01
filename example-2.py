from kucoin.client import Trade
from kucoin.client import Market
import pandas as pd
from time import sleep

api_key = '60491b8da682810006e2f600'
api_secret = 'a79226df-55ce-43d0-b771-20746e338b67'
api_passphrase = 'algotrading101'

m_client = Market(url='https://api.kucoin.com')
client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)

while True:
    try:
        btc_old = m_client.get_ticker('BTC-USDT')
        print('The price of BTC at {} is:'.format(pd.Timestamp.now()), btc_old['price'])
    except Exception as e:
        print(f'Error obtaining BTC data: {e}')

    sleep(300)

    try:
        btc_new = m_client.get_ticker('BTC-USDT')
        print('The price of BTC at {} is:'.format(pd.Timestamp.now()), btc_new['price'])
    except Exception as e:
        print(f'Error obtaining BTC data: {e}')

    percent = (((float(btc_new['bestAsk']) - float(btc_old['bestAsk'])) * 100) / float(btc_old['bestAsk']))

    if percent < 5:
        print('The trade requirement was not satisfied. The percentage move is at ',percent)
        continue

    elif percent >= 5:
        try:
            order = client.create_market_order('ETH-USDT', 'buy', size='5')
            print()
        except Exception as e:
            print(f'Error placing order: {e}')

        sleep(2)

        try:
            check = client.get_order_details(orderId=order['orderId'])
            print(check)
        except Excpetion as e:
            print(f'Error while checking order status: {e}')

        if check['isActive'] == true:
            print ('Order placed at {}'.format(pd.Timestamp.now()))
            break

        else:
            print('Order was canceled {}'.format(pd.Timestamp.now()))
            break
