# -*- coding: utf-8 -*-
import requests

xml = """<?xml version='1.0' encoding='utf-8'?>
<message>
  <proframeHeader>
    <pfmAppName>BIS-KOFIABOND</pfmAppName>
    <pfmSvcName>BISLastAskPrcROPSrchSO</pfmSvcName>
    <pfmFnName>listDay</pfmFnName>
  </proframeHeader>
  <systemHeader></systemHeader>
<BISComDspDatDTO><val1>20170807</val1></BISComDspDatDTO></message>"""
headers = {'Content-Type': 'application/xml'} # set what your server accepts
print(requests.post('http://www.kofiabond.or.kr/proframeWeb/XMLSERVICES/', data=xml, headers=headers).text)
