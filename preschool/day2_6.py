import urllib2

page = urllib2.urlopen("http://www.beans-r-us.biz/prices.html")
bean_text = page.read().decode("utf8")
where = bean_text.find('>$')
start_offset = where+2
end_offset=start_offset+4
price = bean_text[start_offset:end_offset]
print(price)
