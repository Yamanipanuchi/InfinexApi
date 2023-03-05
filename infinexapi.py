#!/usr/bin/python3
import requests, time, traceback, hashlib
import json

class infinex:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.urls = {
            "assets": "https://api.infinex.cc/wallet/assets",
            "networks": "https://api.infinex.cc/wallet/networks",
            "balance": "https://api.infinex.cc/wallet/balances",
            "transactions": "https://api.infinex.cc/wallet/transactions",
            "deposit": "https://api.infinex.cc/wallet/deposit",
            "withdrawInfo": "https://api.infinex.cc/wallet/withdraw/info",
            "withdrawValidate": "https://api.infinex.cc/wallet/withdraw/validate",
            "withdraw": "https://api.infinex.cc/wallet/withdraw",
            "withdrawCancel": "https://api.infinex.cc/wallet/withdraw/cancel",
            "addressBook": "https://api.infinex.cc/wallet/addressbook",
            "addressBookRename": "https://api.infinex.cc/wallet/addressbook/rename",
            "orderBook": "https://api.infinex.cc/spot/orderbook",
            "openOrders": "https://api.infinex.cc/spot/open_orders",
            "open": "https://api.infinex.cc/spot/open_orders/new",
            "cancel": "https://api.infinex.cc/spot/open_orders/cancel"
        }


    def assets(self, symbols = '', search = '', offset = 0):

        data = {}
        if symbols != '': data['symbol'] = symbols
        if search != '': data['search'] = search
        data['offset'] = offset

        req = requests.post(self.urls['assets'], json=data).json()
        return req

    def networks(self, asset):

        data = {}
        data['asset'] = asset
        print (data)

        req = requests.post(self.urls['networks'], json=data).json()
        return req

    def balance(self, symbols = '', search = '', offset = 0):

        data = {}
        data['api_key'] = self.apiKey
        if symbols != '': data['symbol'] = symbols
        if search != '': data['search'] = search
        data['offset'] = offset

        req = requests.post(self.urls['balance'], json=data).json()
        return req

    def transactions(self, asset = '', type = '', status = '', offset = 0):

        data = {}
        data['api_key'] = self.apiKey
        if asset != '': data['asset'] = asset
        if type != '': data['type'] = type
        if status != '': data['status'] = status
        data['offset'] = offset

        req = requests.post(self.urls['transactions'], json=data).json()
        return req

    def deposit(self, asset, network):

        data = {}
        data['api_key'] = self.apiKey
        data['asset'] = asset
        data['network'] = network

        req = requests.post(self.urls['deposit'], json=data).json()
        return req

    def WithdrawInfo(self, asset, network):

        data = {}
        data['api_key'] = self.apiKey
        data['asset'] = asset
        data['network'] = network

        req = requests.post(self.urls['withdrawInfo'], json=data).json()
        return req

    def WithdrawValidation(self, asset, network, address='', memo=''):

        data = {}
        data['api_key'] = self.apiKey
        data['asset'] = asset
        data['network'] = network
        if address != '': data['address'] = address
        if memo != '': data['memo'] = memo

        req = requests.post(self.urls['withdrawValidation'], json=data).json()
        return req

    def Withdraw(self, asset, network, address, amount, fee, memo = '', adbl_name = ''):

        data = {}
        data['api_key'] = self.apiKey
        data['asset'] = asset
        data['network'] = network
        data['address'] = address
        data['amount'] = amount
        data['fee'] = fee
        if memo != '': data['memo'] = memo
        if adbl_name != '': data['adbl_name'] = adbl_name

        req = requests.post(self.urls['withdraw'], json=data).json()
        return req

    def WithdrawCancel(self, xid):

        data = {}
        data['api_key'] = self.apiKey
        data['xid'] = xid

        req = requests.post(self.urls['withdrawCancel'], json=data).json()
        return req

    def addressBook(self, asset='', network=''):

        data = {}
        data['api_key'] = self.apiKey
        if asset != '': data['asset'] = asset
        if network != '': data['network'] = network

        req = requests.post(self.urls['addressBook'], json=data).json()
        return req

    def addressBookRename(self, adbkid, new_name):   

        data = {}
        data['api_key'] = self.apiKey
        data['adbkid'] = adbkid
        data['new_name'] = new_name

        req = requests.post(self.urls['addressBookRename'], json=data).json()
        return req


    def OrderBook(self, market):
        data = {'pair': market}
        req = requests.post(self.urls['orderBook'], json=data).json()
        return req

    def OpenOrders(self, market, offset = 0):
        data = {'api_key': self.apiKey, 'offset': offset, 'filter_pair': market}
        req = requests.post(self.urls['openOrders'], json=data).json()
        return req

    def openOrder(self, market, side, type, tif, price, amount):
        data = {'api_key': self.apiKey, 'pair': market, 'side': side, 'type': type, 'time_in_force': tif, 'price': price, 'amount': amount}
        req = requests.post(self.urls['open'], json=data).json()
        return req

    def cancelOrder(self, obid):

        data = {}
        data['api_key'] = self.apiKey
        data['obid'] = int(obid)

        req = requests.post(self.urls['cancel'], json=data).json()
        return req
