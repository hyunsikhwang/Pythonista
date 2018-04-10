import bs4, requests
import urllib.request
import json

def get_beautiful_soup(url):
	return bs4.BeautifulSoup(requests.get(url).text, "html5lib")

url_phone = "https://www.rooffunding.com/v2/phones/"
url_realestate = "https://www.rooffunding.com/v1/projects/page/1"

def rooffunding_phone(url):

	a = urllib.request.urlopen(url)
	data = json.loads(a.read().decode())
	
	#print(data)
	
	for title in data:
		if title['current_amount_num'] != title['total_amount_num']:
			print('{:10} {:3.0f}%'.format(title['title'], title['current_amount_num'] / title['total_amount_num'] * 100))

	
def rooffunding_realestate(url):

	a = urllib.request.urlopen(url)
	data = json.loads(a.read().decode())
	
	#print(data)
	
	for title in data['projects']:
		if title['current_amount_num'] != title['total_amount_num']:
			print('{:10} {:3.0f}%'.format(title['title'], title['current_amount_num'] / title['total_amount_num'] * 100))


rooffunding_phone(url_phone)
rooffunding_realestate(url_realestate)

print("-------------------------------------")
