#pulls down current price of cryptocurrency provided as a command line argument when executing the script.
#ex: python prices-polybar-coinmarketcap.py bitcoin (this will retrieve the current price of bitcoin and print it out using stdout
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

#check if there is an internet connection, if so, retrieve the price and display it, if not display a dash
if is_connected() == True:

    tickerURL = "https://api.coinmarketcap.com/v1/ticker/" + sys.argv[1]
    request = requests.get(tickerURL)
    data = request.json()
    price = data[0]["price_usd"]
    pricef = float(price)
    print('{:.{prec}f}'.format(pricef, prec=0))

else:
    print('-')

