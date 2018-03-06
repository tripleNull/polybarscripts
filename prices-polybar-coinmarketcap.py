import sys
import netcris

pricef = float(netcris.retrieve_price(sys.argv[1]))
print('{:.{prec}f}'.format(pricef, prec=0))

