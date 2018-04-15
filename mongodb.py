import console
from pymongo import MongoClient
import configparser
import json


console.clear()

with open('config.json', 'r') as f:
	config = json.load(f)

def m_db_init():
	MONGO_HOST = config['mlab']['MONGO_HOST']
	MONGO_PORT = config['mlab']['MONGO_PORT']
	MONGO_DB = config['mlab']['MONGO_DB']
	MONGO_USER = config['mlab']['MONGO_USER']
	MONGO_PASS = config['mlab']['MONGO_PASS']
	
	connection = MongoClient(MONGO_HOST, MONGO_PORT)
	db = connection[MONGO_DB]
	check = db.authenticate(MONGO_USER, MONGO_PASS)
	collection = db['test_KBO']
	
	return collection

collection = m_db_init()
a = collection.find({})
a = collection.find({'DATE':'20180415'})
for item in a:
	#print('{0} {1} {2:.1f}%'.format(item['업체명'], item['상품명'], float(item['모집률'])))
	print(item['NO'], item['TEAM'], item['R'], item['STATUS'])
