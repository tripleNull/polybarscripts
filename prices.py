import netcris

#check if there is an internet connection, if so, retrieve the price and display it, if not display a dash

with open('/home/matt/Documents/prices.txt', 'w') as f:
    	print(netcris.retrieve_price("bitcoin"), ',', netcris.retrieve_price("ethereum"), ',', netcris.retrieve_price("litecoin"), file=f)
