import bs4, requests
import urllib.request
import json

def get_beautiful_soup(url):
    return bs4.BeautifulSoup(requests.get(url).text, "html5lib")

url = "https://www.rooffunding.com/v2/phones/"
soup = get_beautiful_soup(url)

a = urllib.request.urlopen(url)
data = json.loads(a.read().decode())

#print(data)

for title in data:
	if title['current_amount_num'] != title['total_amount_num']:
		print('{:10} {:3.0f}%'.format(title['title'], title['current_amount_num'] / title['total_amount_num'] * 100))
print("-------------------------------------")
