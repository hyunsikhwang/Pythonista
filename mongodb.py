import console
from pymongo import MongoClient
import configparser
import json
from datetime import datetime

console.clear()

today = datetime.today().strftime("%Y%m%d")
json_name = 'config.json'

def import_json(json_name):
	with open(json_name, 'r') as f:
		config = json.load(f)
	
	return config


def m_db_init(config, coll):
	MONGO_HOST = config['mlab']['MONGO_HOST']
	MONGO_PORT = config['mlab']['MONGO_PORT']
	MONGO_DB = config['mlab']['MONGO_DB']
	MONGO_USER = config['mlab']['MONGO_USER']
	MONGO_PASS = config['mlab']['MONGO_PASS']
	
	connection = MongoClient(MONGO_HOST, MONGO_PORT)
	db = connection[MONGO_DB]
	check = db.authenticate(MONGO_USER, MONGO_PASS)
	collection = db[coll]
	
	return collection
	
	
config = import_json(json_name)
coll = 'test_P2P_Assets'
coll = 'test_P2P_Lists'
#coll = 'test_KBO'
collection = m_db_init(config, coll)
a = collection.find({})
#a = collection.find({'DATE':today})
for item in a:
	print('{0} {1} {2:.1f}%'.format(item['업체명'], item['상품명'], float(item['모집률'])))
	#print(item['NO'], item['TEAM'], item['R'], item['STATUS'])
	i = 0
	fmt = []
	for key, value in item.items():
		if key != '_id':
			fmt.append('{' + str(i) + '}')
			i = i + 1
			#print(key, value if isinstance(value, (int, float, complex)) else value)
	print(' '.join(fmt).format())
