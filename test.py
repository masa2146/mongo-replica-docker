import pymongo
MONGO_URI = "mongodb://catalog:123456@127.0.0.1:27017,127.0.0.1:27018,127.0.0.1:27019,127.0.0.1:27020/replicaSet=rs0"
client = pymongo.MongoClient(MONGO_URI)
print("Databases - " + str(client.list_database_names()))