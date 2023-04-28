from mongo import adapter
from datetime import datetime


class MessageManager():
    def __init__(self, dburl, db):
        # "mongodb://localhost:27017/"
        self.dbAdapter = adapter.MongoAdapter(dburl, db)

    def saveMessage(self, _from, _to, _message):
        now = datetime.now()
        self.dbAdapter.saveRecord({"from": _from, "to": _to, "message": _message, "time": now, "status": "unread"})

    def fetchUnread(self, _user):
        _filter = {"to": _user, "status": "unread"}
        records = self.dbAdapter.fetchRecord(_filter)
        self.dbAdapter.updateRecord(_filter,{"status":"read"})
        return records
