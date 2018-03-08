import sys
import netcris

# surreounded this in a try/except block as retrieve_price can return a string of '-' when there is no internet connection
try:
    pricef = float(netcris.retrieve_price(sys.argv[1]))
    print('{:.{prec}f}'.format(pricef, prec=0))
except ValueError:
    print('-')
