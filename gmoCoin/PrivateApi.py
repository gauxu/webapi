import requests
import json
import hmac
import hashlib
import time
from datetime import datetime

# PrivateApiへの接続にはその都度accessTokenを取得する必要有
def connect():
    apiKey    = GMO_API_KEY
    secretKey = GMO_SECRET_KEY

    timestamp = '{0}000'.format(int(time.mktime(datetime.now().timetuple())))
    method    = 'POST'
    endPoint  = 'https://api.coin.z.com/private'
    path      = '/v1/ws-auth'

    text = timestamp + method + path
    sign = hmac.new(bytes(secretKey.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()
    headers = {
        "API-KEY": apiKey,
        "API-TIMESTAMP": timestamp,
        "API-SIGN": sign
    }
    res = requests.post(endPoint + path, headers=headers)
    print(res.json())
    print(json.dumps(res.json(), indent=2))
    return(res.json()["data"])

