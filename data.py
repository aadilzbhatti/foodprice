import urllib.request as url
from bs4 import BeautifulSoup
import csv

def get_prices(link='http://www.fastfoodmenuprices.com/mcdonalds-prices/'):
	req = url.Request(link, headers={'User-Agent' : "Magic Browser"})
	response = url.urlopen(req)
	html = response.read()

	soup = BeautifulSoup(html, 'html.parser')
	data = {}
	for item in soup.findAll('td'):
		if item.attrs['class'] == ['column-1']:
			name = item.string
		if item.attrs['class'] == ['column-3']:
			children = item.findChildren()
			for child in children:
				try:
					if child.attrs['class'] == ['table-press-ori']:
						data[name] = float(child.attrs['value'][1:])
				except KeyError:
					pass
	return data

def get_nutrition():
	data = {}
	with open('other.csv') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[0] == 'Name':
				continue
			else:
				data[row[0]] = int(row[3])
	return data