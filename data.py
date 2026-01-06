from dotenv import load_dotenv,find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())
password=os.environ.get("MONGOO_PWB")
connection_string = f"mongodb+srv://majjigapuharsithreddy_db_user:{password}@data.ya5e90s.mongodb.net/"
client=MongoClient(connection_string)
dbs=client.list_database_names()
test_db=client.sample_mflix
collections=test_db.list_collection_names()
print(collections)
def insert_test_doc():
    collection=test_db.sample_mflix
    test_documents={
        "name":"Gaphu",
        "type":"Database User",
        "jkdgyd":"JKDGDU"
    }
    inserted_id=collection.insert_one(test_documents).inserted_id
    print(inserted_id)
production=client.production
person_collection=production.persons
def create_documents():
    first_names=["Gaphu","Reddy","Sithu","Majji","Pawan"]
    last_names=["Majji","Reddy","Kumar","Singh","Sharma"]   
    age=[21,22,23,24,25]
    docs=[]
    for first_names,last_names,age in zip(first_names,last_names,age):
        document={
            "first_name":first_names,
            "last_name":last_names,
            "age":age
        }
        docs.append(document)
    person_collection.insert_many(docs)
create_documents()


