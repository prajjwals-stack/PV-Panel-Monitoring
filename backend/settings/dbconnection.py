from pymongo import MongoClient


connection=MongoClient("mongodb://localhost:27017")
db=connection["PV-Panel-Monitoring"]