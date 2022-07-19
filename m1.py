import pymongo
client = pymongo.MongoClient("mongodb+srv://sarika:deeshu12@cluster0.y7x9p.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name":"sarika","email":"sarika25in@gmail.com","surname":"kanuganti"}
d = {"name":"sarika","email":"sarika25in@gmail.com","surname":"kanuganti"}
d = {"name":"sarika","email":"sarika25in@gmail.com","surname":"kanuganti"}
db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d)