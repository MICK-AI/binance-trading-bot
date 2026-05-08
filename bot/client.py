import hmac
import time
import hashlib
import requests
from urllib.parse import urlencode

API_KEY = "YOUR_API_KEY"
SECRET_KEY = "YOUR_SECRET_KEY"

BASE_URL = "https://demo-fapi.binance.com"

endpoint = "/fapi/v1/order"

def place_market_order(symbol,side,quantity):

    url = BASE_URL +endpoint

    params = {
        "symbol" : symbol,
        "side"   : side,
        "type"   : "MARKET",
        "quantity" : quantity,
        "timestamp": int(time.time()*1000)
    }

    query_string = urlencode(params)

    signature = hmac.new(
        SECRET_KEY.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()

    params["signature"] = signature

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    response = requests.post(
        url,
        headers=headers,
        params=params
    )

    return response.json()

def place_limit_order(symbol, side, quantity, price):

    endpoint = "/fapi/v1/order"

    url = BASE_URL + endpoint

    params = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC",
        "timestamp": int(time.time() * 1000)
    }

    query_string = urlencode(params)

    signature = hmac.new(
        SECRET_KEY.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()

    params["signature"] = signature

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    response = requests.post(
        url,
        headers=headers,
        params=params
    )

    return response.json()