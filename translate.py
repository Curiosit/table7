#conda install -c anaconda pymongo
#conda install -c conda-forge python-dotenv

import pandas as pd
from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv
import csv

load_dotenv()




user = os.getenv('MONGODB_USER')
password = os.getenv('MONGODB_PASSWORD')
uri = os.getenv('MONGODB_URI')

""" mongoClient = MongoClient(uri)
MongoClient(username=user, password=password)
mongoClient.admin.command('ping')

db = mongoClient['material-library']
db.command('ping')
collection = db['epds'] """
csvfilepath = 'src/tabel7.csv'
#csvfile = open('src/tabel7.csv', 'r')
reader = pd.read_csv(csvfilepath,encoding = 'UTF-8')
data_json = json.loads(reader.to_json(orient='records'))
print(data_json[1])
print(data_json[1]['NAVN'])
jsondata = []
i = 0
for row in data_json:
    i = i + 1
    if i < 1000:
        rowjson = {
            'name':row['NAVN'],
            
        }
        print (rowjson)
        #jsondata.append(rowjson)
        #collection.insert(rowjson)
print(jsondata)
""" for row in data_json:
    print(row)
    collection.insert(row) """
#collection.insert(data_json)




