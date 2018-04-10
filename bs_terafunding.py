import bs4, requests

def get_beautiful_soup(url):
	return bs4.BeautifulSoup(requests.get(url).text, "html5lib")

def terafunding(url):
	soup = get_beautiful_soup(url)

	pkg_list = soup.find_all("div", "funditem js-link")
	pkg_list = soup.find_all("div", attrs={"data-status" : ["1","2"]})
	
	#print(pkg_list)
	
	count = 1
	for i in pkg_list:
		title = i.find_all("div", "title")
		progress = i.find_all("span", "pull-right js_progress_value")
		print(str(title[0].text), str(progress[0].text))
		count = count + 1
	print("-------------------------------------")


import sqlite3

def create_table():
	
	# Create table
	c.execute('''CREATE TABLE test_tf
	(company text, item text, status real)''')
	conn.commit()


def insert_record():
	
	# Insert a row of data
	c.execute("INSERT INTO test_tf VALUES ('테라펀딩','112차',0.51)")
	conn.commit()
	
def delete_record():
	c.execute("DELETE FROM test_tf WHERE company = '테라펀딩'")
	conn.commit()

url = 'https://www.terafunding.com/Invest'
terafunding(url)

'''
conn = sqlite3.connect('p2p_invest.db')

c = conn.cursor()

#create_table()
insert_record()
#delete_record()

c.execute("select * from test_tf")
print(c.fetchall())

conn.close()
'''
