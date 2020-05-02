from pymongo import MongoClient
from bson import Code
import re

client = MongoClient()

def collection_names(db_name):
    db = client[db_name]
    collection_names = db.list_collection_names()
    return collection_names

def db_names():
    dbs = MongoClient().list_database_names()
    return dbs

def get_keys(db_name, collection):
    db = client[db_name]
    collection = db[collection]

    mapper = Code("""
    function() {
                  for (var key in this) { emit(key, null); }
               }
    """)
    reducer = Code("""
        function(key, stuff) { return null; }
    """)

    distinctThingFields = collection.map_reduce(mapper, reducer
        , out = {'inline' : 1}
        , full_response = True)
    res = [key['_id'] for key in distinctThingFields['results'] if True]

    return res