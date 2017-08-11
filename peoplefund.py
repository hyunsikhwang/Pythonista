import bs4, requests
import urllib.request
import json

def get_beautiful_soup(url):
    return bs4.BeautifulSoup(requests.get(url).text, "html5lib")

url = "https://static.peoplefund.co.kr/showcase/listGetAjax/list/?v=201707181614_1200"
soup = get_beautiful_soup(url)

a = urllib.request.urlopen(url)
data = json.loads(a.read().decode())

#print(data)

for title in data['data']['list']:
	if title['investor_amount'] != title['loan_application_amount']:
		print('{:10} {:3.0f}%'.format(title['seo_title'], title['investor_amount'] / title['loan_application_amount'] * 100))
print("-------------------------------------")
