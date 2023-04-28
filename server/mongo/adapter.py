import pymongo


class MongoAdapter():
    def __init__(self, dburl, db):
        client = pymongo.MongoClient(dburl)
        db = client[db]
        self.collection = db["messages"]

    def saveRecord(self, record):
        try:
            self.collection.insert_one(record)
        except Exception as e:
            error = e
            print(e)

    def fetchRecord(self, _filter):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["flask_tutorial"]
        collection = db["messages"]
        records = []
        for x in self.collection.find(_filter):
            records.append(x)
        return records

    def updateRecord(self, _filter, record=None):
        try:
            result = self.collection.update_many(_filter, {"$set": record})
            print(result)
        except Exception as e:
            print(e)
