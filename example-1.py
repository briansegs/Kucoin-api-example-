from kucoin.client import Trade
from kucoin.client import Market
import pandas as pd
from time import sleep

api_key = '<api_key>'
api_secret = '<api_secret>'
api_passphrase = '<api_passphrase>'

m_client = Market(url='https://api.kucoin.com')
client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)

while True:
    try:
        btc = m_client.get_ticker('BTC-USDT')
        print('The price of BTC at {} is:'.format(pd.Timestamp.now()), btc['price'])
    except Exception as e:
        print(f'Error obtaining BTC data: {e}')

    if float(btc['bestAsk']) < 57200.00:
        continue

    elif float(btc['bestAsk']) >= 57200.00:
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