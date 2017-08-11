import bs4, requests

def get_beautiful_soup(url):
    return bs4.BeautifulSoup(requests.get(url).text, "html5lib")

soup = get_beautiful_soup('https://www.popfunding.com/pf/social')
#print(soup.prettify())
pkg_list = soup.find_all("div", "sub-info")
pkg_details = soup.find_all("div", "status-info")

idx = 0
m_title = []
m_dtls = []
m_name = []

for i in pkg_list:
	title = i.find_all('strong')
	m_list = title[0].text
	m_title.append(m_list)
#print(pkg_details)
for i in pkg_details:
	details_1 = i.find_all('p', 'price')
	details_2 = i.find_all('p', 'progress ')
	for itm in details_1:
		l_details_1 = itm.find_all('em', 'convert')
	m_details_1 = l_details_1[0].text.replace("원","").replace(",","")
	for itm2 in details_2:
		itm3 = itm2.find_all('span')
		for itm in itm3:
			if itm.text.find('모집금액') > 0:
				m_details_2 = itm.text.replace("- 모집금액 ", "").replace("원", "").replace(",", "")
	m_details = int(m_details_2) / int(m_details_1) * 100
	if m_details_1 != m_details_2:
		m_dtls.append(m_title[idx] + '\t' + '{:3.0f}%'.format(m_details))
	idx=idx+1

for itm in m_dtls:
	print(itm)

print("-------------------------------------")
#for i in range(0,count):
#	print(m_name)

# See: http://www.crummy.com/software/BeautifulSoup/bs4/doc for all the things you can do with the soup.
