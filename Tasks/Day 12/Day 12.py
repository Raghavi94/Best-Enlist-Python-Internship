#TASK-12:

#Create a JSON of all object types and import the JSON into a SQL Database

import json
from pymongo import MongoClient
myclient = MongoClient("mongodb://localhost:27017/")

a={
    "firstName":"Joe",
    "lastName":"Jacky",
    "age":20,
    "hobbies":["Jogging","Swimming","Dancing"],
    "Student":True,
    "Average":70.23
    },{
    "firstName":"Milind",
    "lastName":"Soman",
    "age":19,
    "hobbies":["Singing","Drawing","Writing poems"],
    "Student":True,
    "Average":84.57
    }
with open("doc.json","w") as f:
    json.dump(a,f,indent=4)


#from pymongo import MongoClient
#myclient=MongoClient("mongodb://localhost:4000/")
db=myclient["mongdb"]
Collection=db["info"]
with open("doc.json") as f:
    data=json.load(f)
if isinstance(data,list):
    Collection.insert_many(data)
else:
    Collection.insert_one(data)

    

