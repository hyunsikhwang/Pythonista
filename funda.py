import bs4, requests

def get_beautiful_soup(url):
    return bs4.BeautifulSoup(requests.get(url).text, "html5lib")

soup = get_beautiful_soup('https://www.funda.kr/v2/investment')
#print(soup.prettify())
pkg_list = soup.find_all("div", "merchandise_inner_box")
pkg_details = soup.find_all("div", "merchandise_details")
progress = soup.find_all("div", "merchandise_progress_bar")

idx = 0
m_title = []
m_dtls = []
m_name = []

for i in pkg_list:
	title = i.find_all('span')
	m_list = title[0].text
	m_title.append(m_list)

for i in pkg_details:
	details = i.find_all('span')
	m_details = details[1].text.replace(" ", "").replace('\n','').replace('\r','')
	#m_dtls.append(m_title[idx] + " / " + m_details)
	m_dtls.append(m_title[idx])
	idx=idx+1

idx = 0
for i in progress:
	#amt = i.find_all("span", "pull-left")
	#m_list = amt[0].text
	ratio = i.find_all("span", "pull-right")
	m_list = ratio[0].text.replace('\n','').replace('\r','')
	if m_list != '100%':
		m_name.append(m_dtls[idx] + " / " + m_list)
	idx=idx+1

for i in m_name:
	print(i)

print("-------------------------------------")
#for i in range(0,count):
#	print(m_name)

# See: http://www.crummy.com/software/BeautifulSoup/bs4/doc for all the things you can do with the soup.
