import sys
import requests
import json
import socket

REMOTE_SERVER = "archlinux.org"

#checks if there is an internet connection
def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

# grab the price of the selected crypto currency
def retrieve_price(crypto):
    if is_connected() == True:
        tickerURL = "https://api.coinmarketcap.com/v1/ticker/" + crypto
        request = requests.get(tickerURL)
        data = request.json()
        price = data[0]["price_usd"]
        return price
    else:
        return "-"

