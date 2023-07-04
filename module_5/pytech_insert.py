#   Ashlyn Barrett
#   7-6-2023
#   Module 5.3
#

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.9yphtky.mongodb.net/"
client = MongoClient(url)
db = client.pytech

students = db.students

sam = {
    "student_id": "1007",
    "first_name": "Sam",
    "last_name": "Jones",
}
sam_student_id = students.insert_one(sam).inserted_id
print("Inserted student record Sam Jones into the students collection with document_id " + str(sam_student_id))

biff = {
    "student_id": "1008",
    "first_name": "Biff",
    "last_name": "Paval",
}
biff_student_id = students.insert_one(biff).inserted_id
print("Inserted student record Biff Paval into the students collection with document_id " + str(biff_student_id))

cletus = {
    "student_id": "1009",
    "first_name": "Cletus",
    "last_name": "Porter",
}
cletus_student_id = students.insert_one(cletus).inserted_id
print("Inserted student record Cletus Porter into the students collection with document_id " + str(cletus_student_id))
    
input("End of program, press any key to exit...")