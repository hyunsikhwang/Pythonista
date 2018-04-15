#!/usr/bin/python

from pymongo import MongoClient

def m_db_init():
	MONGO_DB = "cluster0"

	connection = MongoClient('mongodb://realg:ofsm9dmdb!@cluster0-shard-00-00-k5utu.mongodb.net:27017,cluster0-shard-00-01-k5utu.mongodb.net:27017,cluster0-shard-00-02-k5utu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')

	db = connection[MONGO_DB]

	return db


def m_db_upsert():
	MONGO_DB = "cluster0"

	connection = MongoClient('mongodb://realg:ofsm9dmdb!@cluster0-shard-00-00-k5utu.mongodb.net:27017,cluster0-shard-00-01-k5utu.mongodb.net:27017,cluster0-shard-00-02-k5utu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')

	db = connection[MONGO_DB]
	collection = db['test-collection']
	collection.insert_one({'test':'테스트입력'})


m_db_upsert()
