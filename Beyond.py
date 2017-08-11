import bs4, requests
import urllib.request
import json

def get_beautiful_soup(url):
    return bs4.BeautifulSoup(requests.get(url).text, "html5lib")

url = "https://api.30cut.com/fund/invest/goods?limit=9&page=1"
soup = get_beautiful_soup(url)

a = urllib.request.urlopen(url)
data = json.loads(a.read().decode())

#print(data)

for title in data:
	if title['investTotalMoney'] != title['finalMoney']: 
		print('{:10} {:3.0f}%'.format(title['title'], title['investTotalMoney']/title['finalMoney']*100))
print("-------------------------------------")

