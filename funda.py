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
	ratio = i.find_all("span", "pull-right")
	m_list = ratio[0].text.replace('\n','').replace('\r','')
	if m_list != '100%':
		m_name.append(m_dtls[idx] + ' ' + m_list)
	idx=idx+1

#for i in m_name:
	#print(i)

#print("-------------------------------------")

import ui

f = (0, 0, 95, 300)
tbl = ui.TableView(frame=f, name='펀다')
tbl.width, tbl.height = 95, 270

tbl.data_source = ui.ListDataSource(items=m_name)
tbl.data_source.font=('<system>',14)
tbl.row_height=30
tbl.separator_color='lightblue'
tbl.present('sheet', title_bar_color = 'lightblue')
#for i in range(0,count):
#	print(m_name)

