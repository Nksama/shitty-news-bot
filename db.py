from pymongo.mongo_client import MongoClient
import os

class NewsDb():
    def __init__(self):
        self.client = MongoClient(os.environ['DBURL'])
        self.db = self.client["bot"]["news"]

    def check(self , news):
        x = self.db.find_one(news)
        if x is None:
            return False
        else:
            return True
        
    def findnews(self , news):
        x = self.db.find_one(news)
        return x

    def add_news(self , news : dict):
        self.db.insert_one(news)

    def replace_news(self , news1 , news2):
        self.db.replace_one(news1 , news2)
        