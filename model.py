from pymongo import MongoClient
from flask import session

client = MongoClient()
db = client['Amazon_Website']

def check_user(indb_username):
	query = {'username':indb_username}
	result = db['users'].find_one(query)
	return result

def add_user_Todb(todb_byussername):
	db['users'].insert_one(todb_byussername)