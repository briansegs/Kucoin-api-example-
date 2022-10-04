import symbol
import ccxt
import pandas as pd
import config as c

kc_futures = ccxt.kucoinfutures({
    'enableRateLimit': True,
    'apiKey': c.kc_futures['API_KEY'],
    'secret': c.kc_futures['API_SECRET'],
    'password': c.kc_futures['API_PASSPHRASE'],
})

symbol = 'XBTUSDTM'

def ask_bid(symbol=symbol):
    ob = kc_futures.fetch_order_book(symbol)
    ask = ob['asks'][0][0]
    bid = ob['bids'][0][0]

    print(f'ask: {ask} | bid: {bid}')

    return ask, bid

ask_bid()