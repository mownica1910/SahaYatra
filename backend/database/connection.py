from pymongo import MongoClient

MONGODB_URI = "mongodb://localhost:27017"
DATABASE_NAME = "sahayatra"

client = MongoClient(MONGODB_URI)

db = client[DATABASE_NAME]