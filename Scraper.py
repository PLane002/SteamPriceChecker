from bs4 import BeautifulSoup
from urllib2 import urlopen
import sys
import string

#Simple program that scans the steam page of any given game (not package) and prints out the title and price listed on steam

def get_steam_prices(page):
	html = urlopen(page).read()
	soup = BeautifulSoup(html,"lxml")
	title_section = soup.find("title").string
	price_section = soup.find("div","game_purchase_price").string
	#print ("title: "+title_section)
	s = price_section
	for c in "\t\n\r":
		s = string.replace(s,c,"")
	#print ("price: "+s)
	print title_section+": "+s
	

get_steam_prices("http://store.steampowered.com/app/71250/") #Sonic Adventure DX
get_steam_prices("http://store.steampowered.com/app/213610/") #Sonic Adventure 2
get_steam_prices("http://store.steampowered.com/app/71340/") #Sonic Generations



