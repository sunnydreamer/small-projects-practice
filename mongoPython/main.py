from pymongo import MongoClient
import datetime 


cluster = "mongodb+srv://sunny:sunny@cluster0.1krhqqx.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(cluster)

print(client.list_database_names())

db = client.test

print(db.list_collection_names())

todo1 = {"name": "Patrick", "text":"My first to do", "status":"open","tags":["python", "coding"], "date":datetime.datetime.utcnow()}

todos = db.todos

# result = todos.insert_one(todo1)

todo2 = [{"name": "Patrick", "text":"My second to do", "status":"open","tags":["python", "coding"], "date":datetime.datetime.utcnow()},{"name": "Mary", "text":"My first to do", "status":"open","tags":["c++", "coding"], "date":datetime.datetime(2021,1,1,10,45)}]

# result = todos.insert_many(todo2)

# print(todos.count_documents({"name": "Patrick"}))
# print(todos.count_documents({"tags": "c++"}))

# d = datetime.datetime(2021,2,1)
# results = todos.find({"date": {"$lt": d}}) 

# for result in results:
#     print(result)


# results = todos.find({"date": {"$lt": d}}).sort("name")



# result = todos.find_one({"name": "Patrick"})
# result = todos.find_one({"name": "Patrick", "text":"My second to do"})
# result = todos.find_one({"tags": "c++"})
# from bson.objectid import ObjectId
# result = todos.find({"_id": ObjectId("641bb281a1946072945f47a9")})

# results = todos.find({"name": "Patrick"})
# print(list(results))

# for result in results:
#     print(result)

# from bson.objectid import ObjectId
# result = todos.delete_one({"_id":ObjectId("641bb281a1946072945f47a9")})

# result = todos.delete_many({"name": "Patrick"})

result = todos.update_one({"tag:":"c++"}, {"$set": {"status": "done"}})
result = todos.update_one({"tag:":"c++"}, {"$unset": {"status": None}})