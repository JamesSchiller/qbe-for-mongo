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

def query(db_name, collection_name, keynames, sorts, conditions):
    selections = {}
    projections = {}
    sort = {}

    db = client[db_name]
    collection = db[collection_name]

    projections.update({"_id": False})

    for i, keyname in enumerate(keynames):
        if conditions[i]:
            if '!=' in conditions[i]:
                conditions[i] = conditions[i].replace("!=", "").strip()
                selections.update({keyname: {"$ne": conditions[i]}})
            elif '>=' in conditions[i]:
                conditions[i] = conditions[i].replace(">=", "").strip()
                selections.update({keyname: {"$gte": int(conditions[i])}})
            elif '>' in conditions[i]:
                conditions[i] = conditions[i].replace(">", "").strip()
                selections.update({keyname: {"$gt": int(conditions[i])}})
            elif '<=' in conditions[i]:
                conditions[i] = conditions[i].replace("<=", "").strip()
                selections.update({keyname: {"$lte": int(conditions[i])}})
            elif '<' in conditions[i]:
                conditions[i] = conditions[i].replace("<", "").strip()
                selections.update({keyname: {"$lt": int(conditions[i])}})
            elif 'like' in conditions[i].lower():
                conditions[i] = conditions[i].replace("like", "").replace("Like", "").replace("LIKE", "").strip()
                conditions[i] = conditions[i].replace("'", "")
                if conditions[i][0] == "%" and conditions[i][len(conditions[i])-1] == "%":
                    conditions[i] = conditions[i].replace("%", "")
                elif conditions[i][0] == "%" and conditions[i][len(conditions[i])-1] != "%":
                    conditions[i] = conditions[i].replace("%", "")
                    conditions[i] += "$"
                elif conditions[i][0] != "%" and conditions[i][len(conditions[i])-1] == "%":
                    conditions[i] = conditions[i].replace("%", "")
                    conditions[i] = "^" + conditions[i]
                selections.update({keyname: {"$regex": conditions[i]}})
            elif '=' in conditions[i] or '' in conditions[i]: # default is =
                conditions[i] = conditions[i].replace("=", "").strip()
                try: 
                    conditions[i] = int(conditions[i])
                except ValueError:
                    print("leave string a string")
                selections.update({keyname: {"$eq": conditions[i]}})
        if sorts[i]:
            if sorts[i][0:3].lower() == "asc":
                sort.update({keyname: 1})
            elif sorts[i][0:3].lower() == "des":
                sort.update({keyname: -1})
                
        projections.update({keyname: 1}) # can make this show only if show is checked

    if keynames:
        res = collection.find(selections, projections)
        for k, v in sort.items():
            res.sort(k, v)
    else:
        res = []

    resnoblanks = [ele for ele in res if ele != {}]

    return list(resnoblanks)