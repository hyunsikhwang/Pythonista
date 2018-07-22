# -*- coding: utf-8 -*-
import requests
import bs4
import xml.etree
from datetime import datetime, timedelta
import console
import json


def post_beautiful_soup(url, payload):
	return bs4.BeautifulSoup(requests.post(url, data=payload).text, "html5lib")


def get_beautiful_soup(url):
	return bs4.BeautifulSoup(requests.get(url).text, "html5lib")


def millis():
	return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)

console.clear()

milli_timestamp = millis()
#print(milli_timestamp)

end_dd = datetime.today().strftime("%Y%m%d")
strt_dd = (datetime.now() - timedelta(days=7)).strftime("%Y%m%d")

data_type = {}
data_type['IDX'] = 0
data_type['PER'] = 1
data_type['PBR'] = 2

xx = 'IDX'

url_1 = []
#지수
url_1.append('http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F10%2F1001%2F10010101%2Fmkd10010101_07&name=selectbox&_=' + str(milli_timestamp))

#PER
url_1.append('http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F13%2F1301%2F13010103%2Fmkd13010103_02&name=selectbox&_=' + str(milli_timestamp))

#PBR
url_1.append('http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F13%2F1301%2F13010104%2Fmkd13010104_02&name=selectbox&_=' + str(milli_timestamp))

#url_2 = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx?type=1&ind_type=1001&period_strt_dd=20170804&period_end_dd=20170811&pagePath=%2Fcontents%2FMKD%2F10%2F1001%2F10010101%2FMKD10010101.jsp&code=' + OTP + '&pageFirstCall=Y'
url_2 = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx'


pagePath = []
#지수
pagePath.append('/contents/MKD/10/1001/10010101/MKD10010101.jsp')

#PER
pagePath.append('/contents/MKD/13/1301/13010103/MKD13010103.jsp')

#PBR
pagePath.append('/contents/MKD/13/1301/13010103/MKD13010104.jsp')


headers = {'Content-Type': 'application/xm'} 


for idx in range(3):
	#MktData = get_beautiful_soup(url_2)
	OTP = get_beautiful_soup(url_1[idx]).find('body').text
	#print(OTP)
	if idx == 0:
		#지수
		payload = {'type':'1', 'ind_type':'1001', 'period_strt_dd':strt_dd, 'period_end_dd':end_dd, 'pagePath':'pagePath:'+pagePath[0],'code':OTP, 'pageFirstCall':'Y'}
	elif idx == 1:
		#PER
		payload = {'type':'kospi', 'period_selector':'day', 'fromdate':strt_dd, 'todate':end_dd, 'pagePath':'pagePath:'+pagePath[1],'code':OTP}
	elif idx == 2:
		#PBR
		payload = {'type':'kospi', 'period_selector':'day', 'fromdate':strt_dd, 'todate': end_dd, 'pagePath':'pagePath:'+pagePath[2],'code':OTP}

	MktData = post_beautiful_soup(url_2, payload)
	#print(MktData)
	print(idx)

	data = json.loads(MktData.text)

	if idx == 0:
		print(data['block1'][0]['work_dt'], data['block1'][0]['indx'])
		print(data['block1'][1]['work_dt'], data['block1'][1]['indx'])
	else:
		print(data['block1'][0]['trd_dd'], data['block1'][0]['idx_type1'], data['block1'][0]['idx_type2'])
		print(data['block1'][1]['trd_dd'], data['block1'][1]['idx_type1'], data['block1'][1]['idx_type2'])
