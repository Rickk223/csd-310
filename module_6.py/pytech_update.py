""" 
    Title: pytech_update.py
    Author: Ricardo Guillen Vergara
    Date: 4/13/2021
    Description: Test program for updating a document in the pytech collection
"""

import pymongo

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.wg5hw.mongodb.net/pytech?retryWrites=true&w=majority"
    

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("Student ID: " + doc["student_id"]) 
    print("First Name: " + doc["first_name"])	
    print("Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Oakenshield II"}})

# find and display the updated student document with new last name
wyatt = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID: " + wyatt["student_id"]) 
print("First Name: " + wyatt["first_name"])
print("Last Name: " + wyatt["last_name"] + "\n")