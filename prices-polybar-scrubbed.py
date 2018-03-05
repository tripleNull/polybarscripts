from coinbase.wallet.client import Client
import socket

REMOTE_SERVER = "archlinux.org"

#checks if there is an internet connection first
def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

#check if there is an internet connection, if so, retrieve the price and display it, if not display a dash
isConnected = is_connected()

if isConnected == True:

    client = Client(
       '<api key>', 
       '<api secret>')

    # Make the request
    price = client.get_spot_price(currency_pair = 'BTC-USD')

    print('', price.amount)

else:
    print ('-')
