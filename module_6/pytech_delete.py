""" 
    Title: pytech_delete.py
    Author: Ricardo Guillen Vergara
    Date: 4/14/2021
    Description: Test program for deleting documents from the pytech collection
"""

import pymongo

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.wg5hw.mongodb.net/pytech?retryWrites=true&w=majority"
    
client = MongoClient(url)

#connect to database in mongodb
db = client.pytech

# define variable for students collection
students = db.students

# find all students in the collection 
student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("Student ID: " + doc["student_id"]) 
    print("First Name: " + doc["first_name"])	
    print("Last Name: " + doc["last_name"] + "\n")

# test document with new student data
test_doc = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}

# inserting the test document into MongoDB atlas 
test_doc_id = students.insert_one(test_doc).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# find_one() method by student_id 1010
student_test_doc = students.find_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("Student ID: " + student_test_doc["student_id"]) 
print("First Name: " + student_test_doc["first_name"]) 
print("Last Name: " + student_test_doc["last_name"] + "\n")

#delete_one method to remove the student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find all students in the collection 
new_student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#using loop to output the results of all the collections
# new student John Doe ID 1010 should not come up here
for doc in new_student_list:
    print("Student ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"] + "\n")
