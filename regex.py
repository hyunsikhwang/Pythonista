import re

sourceStr = []

sourceStr.append('제991차 진안군청 인근 연립주택 신축사업 1차')
sourceStr.append('[제172호] 강릉 그린내하우스(공동주택 및 오피스텔) 건축자금 대출 2차')
sourceStr.append('74호 SPEED 스마트폰 투자')

#print(sourceStr)

p = re.compile('제[0-9]+차*.|.*[0-9]+호\]*.')
q = re.compile('[0-9]+')

for item in sourceStr:
	m = p.findall(item)
	n = q.findall(m[0])
	a = item.replace(m[0], '')
	print(n[0], a)
