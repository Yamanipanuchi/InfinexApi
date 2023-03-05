# InfinexApi for Python 3

from InfinexApi import infinex

Setup API Key
exchange = infinex(apikey)

Get Balance for currency
exchange.getBalance(BPX)

Get orderbook for currency pair
exchange.getOrderBook(BPX/USDT)

Get you current open orders
exchange.getOpenOrders(BPX/USDT)

Cancel current open order
exchange.cancelOrder(650039)

Open new order
exchange.openOrder(BPX/USDT, 'BUY', 'MARKET', 'GTC', '0.013600', '3400')


Hopefully this helps someone.

User my affiliate link if you can! Thank you!
http://infinex.cc/account/register?r=7
