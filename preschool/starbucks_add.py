import urllib2
import time
price = 99.99

price_now= raw_input("do you want to see the price now(Y/N)?")
if price_now == "Y":
	page = urllib2.urlopen("http://beans.itcarlow.ie/prices.html")
	text = page.read().decode("utf8")
	where = text.find(">$")
	start_of_price = where + 2
	end_of_price = start_of_price + 4
	price = float(text[start_of_price:end_of_price])
	print(price)
else:
	while price > 7.00: #if you type command C in terminal, you can cease the succesive show up
		time.sleep(1)
		page = urllib2.urlopen("http://beans.itcarlow.ie/prices.html")
		text = page.read().decode("utf8")
		where = text.find(">$")
		start_of_price = where + 2
		end_of_price = start_of_price + 4
		price = float(text[start_of_price:end_of_price])
print("Buy!") #if you type command B you can see the result w/o termianl