#!/usr/bin/python3
import requests, time, traceback, hashlib
import json

class infinex:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.urls = {
            "balance": "https://api.vayamos.cc/wallet/balances",
            "orderBook": "https://api.infinex.cc/spot/orderbook",
            "openOrders": "https://api.infinex.cc/spot/open_orders",
            "cancel": "https://api.infinex.cc/spot/open_orders/cancel",
            "open": "https://api.infinex.cc/spot/open_orders/new"
        }

    def getBalance(self, market, offset = 0):
        data = {'api_key': self.apiKey, 'offset': offset, 'search': market}
        req = requests.get(self.urls['balance'], json=data).json()
        return req

    def getOrderBook(self, market):
        data = {'pair': market}
        req = requests.get(self.urls['orderBook'], json=data).json()
        return req

    def getOpenOrders(self, market, offset = 0):
        data = {'api_key': self.apiKey, 'offset': offset, 'filter_pair': market}
        req = requests.get(self.urls['openOrders'], json=data).json()
        return req

    def cancelOrder(self, orderId):
        data = {'api_key': self.apiKey, 'obid': orderId}
        req = requests.get(self.urls['cancel'], json=data).json()          
        return req

    def openOrder(self, market, side, type, tif, price, amount):
        print (market, side, type, tif, price, amount)
        data = {'api_key': self.apiKey, 'pair': market, 'side': side, 'type': type, 'time_in_force': tif, 'price': price, 'amount': amount}
        req = requests.post(self.urls['open'], json=data).json()               
        return req



