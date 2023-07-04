# Ashlyn Barrett
# Date 7-6-2023
# Module 5.2

from pymongo import MongoClient

URL = "mongodb+srv://admin:admin@cluster0.9yphtky.mongodb.net/"
client = MongoClient(URL)
db = client.pytech

print(" -- Pytech Collection List --")
print()
print(db.list_collection_names())
print()

input(" End of Program, Press any key to exit...")
