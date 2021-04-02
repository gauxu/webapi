import unittest

import requests
import websocket
import json
from datetime import datetime,date

#usage ex1: python -m unittest -v PublicApiConectingTest.py
#usage ex2: python -m unittest -v PublicApiConectingTest.PublicApiTestMethods

#subject: This test is some ApiConnections.

class PublicApiMethods(unittest.TestCase):
    endPoint = 'https://api.coin.z.com/public'

    def test_exchangeOperation(self):
        path = '/v1/status'
        res= requests.get(self.endPoint + path)
        res.raise_for_status()
        #TODO:必要要素が全て過不足無く揃っておりNullでないことを確かめる
        print(res.json())

    def test_newestRate(self):
        path = '/v1/ticker?symbol=BTC'
        res= requests.get(self.endPoint + path)
        res.raise_for_status()
        #TODO:必要要素が全て過不足無く揃っておりNullでないことを確かめる
        #TODO:statusとsymbolとtimestampの内容の妥当性チェックしたいがendPointをダミー（モック）にして副作用をなくすべき
        self.assertIs(res.status_code,200)
        print(res.json())


if __name__ == '__main__':
    unittest.main()