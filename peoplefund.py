import bs4, requests
import urllib.request
import json

def get_beautiful_soup(url):
	return bs4.BeautifulSoup(requests.get(url).text, "html5lib")

url = "https://static.peoplefund.co.kr/showcase/newlistGetAjax/1/list/?page_size=12&offset=5&status=%ED%88%AC%EC%9E%90%EB%AA%A8%EC%A7%91%EB%A7%88%EA%B0%90%2C%EC%83%81%ED%99%98%EC%A4%91%2C%EC%83%81%ED%99%98%EC%A7%80%EC%97%B0%2C%EC%97%B0%EC%B2%B4%EC%A4%91%2C%EC%9E%A5%EA%B8%B0%EC%97%B0%EC%B2%B4%2C%EB%A7%A4%EA%B0%81%EC%99%84%EB%A3%8C%2C%EC%83%81%ED%99%98%EC%99%84%EB%A3%8C&cate=&search=&v=201804061850_1100"
soup = get_beautiful_soup(url)

a = urllib.request.urlopen(url)
data = json.loads(a.read().decode())

#print(data)
pf_item=[]

for title in data['data']['list']:
	if title['investor_amount'] != title['loan_application_amount']:
		#print('{:10} {:3.0f}%'.format(title['seo_title'], title['investor_amount'] / title['loan_application_amount'] * 100))
		pf_item.append('{:10} {:3.0f}%'.format(title['seo_title'], title['investor_amount'] / title['loan_application_amount'] * 100))
		print(title['seo_title'], title['investor_amount'] / title['loan_application_amount'] * 100)
print("-------------------------------------")
