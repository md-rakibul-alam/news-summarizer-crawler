from pymongo import MongoClient
import os
from .IDatabaseContext import IDatabaseContext

class DatabaseContext(IDatabaseContext):
    def __init__(self):
        mongo_uri = os.getenv("MONGO_URI")
        self.client = MongoClient(mongo_uri)
        self.db = self.client.news_summarizer
        self.collection = self.db.newssummary

    def GetNewsById(self, news_id):
        return self.collection.find_one({"id": news_id})

    def GetNewsByUrl(self, url):
        return self.collection.find_one({"url": url})

    def SaveNews(self, news_object):
        self.collection.insert_one(news_object)
        print(news_object)

if __name__ == "__main__":
    pass