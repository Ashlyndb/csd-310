#Ashlyn  Barrett
#Module 6.2
#Due 07/10/2023

from pymongo import MongoClient

URL = "mongodb+srv://admin:admin@cluster0.9yphtky.mongodb.net/"
client = MongoClient(URL)
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smitty"}})

# find the updated student document 
sam = students.find_one({"student_id": "1007"})
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")
print(" Student ID: " + sam["student_id"] + "\n First Name: " + sam["first_name"] + "\n Last Name: " + sam["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")