""" 
    Title: pytech_queries.py
    Author: Ricardo Guillen Vergara
    Date: 4/10/2021
    Description: Test program for querying the students collection.
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

# find document by student_id
wyatt = students.find_one({"student_id": "1007"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID: " + wyatt["student_id"]) 
print("First Name: " + wyatt["first_name"])
print("Last Name: " + wyatt["last_name"] + "\n")