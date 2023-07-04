#   Ashlyn Barrett
#   7-6-23
#   Module 5.3
#

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.9yphtky.mongodb.net/"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})

print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")

# Finding all students in the collection
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")
    
# Finding one student in the collection
sam = students.find_one({"student_id": "1007"})
print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY--")
print(" Student ID: " + sam["student_id"] + "\n First Name: " + sam["first_name"] + "\n Last Name: " + sam["last_name"] + "\n")

print("End of program, press any key to continue...")