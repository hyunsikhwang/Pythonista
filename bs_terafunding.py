import bs4, requests

def get_beautiful_soup(url):
    return bs4.BeautifulSoup(requests.get(url).text, "html5lib")

soup = get_beautiful_soup('https://www.terafunding.com/Invest')
#print(soup.prettify())
#pkg_list = soup.find_all("a", "merchandise_name")
pkg_list = soup.find_all("div", "funditem js-link")

count = 1
for i in pkg_list:
	title = i.find_all("div", "title")
	progress = i.find_all("span", "pull-right js_progress_value")
	if progress[0].text != '100%':
		print(str(title[0].text), str(progress[0].text))
	count = count + 1

print("-------------------------------------")
# See: http://www.crummy.com/software/BeautifulSoup/bs4/doc for all the things you can do with the soup.
