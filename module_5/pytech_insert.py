import pymongo

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.wg5hw.mongodb.net/pytech?retryWrites=true&w=majority"
    

client = MongoClient(url)

db = client.pytech

""" three student documents"""
# Wyatt Earp data document 
wyatt = {
    "student_id": "1007",
    "first_name": "Wyatt",
    "last_name": "Earp",
    "enrollments": [
        {
            "term": "Spring 2020",
            "gpa": "3.5",
            "start_date": "February 01, 2020",
            "end_date": "May 31, 2020",
            "courses": [
                {
                    "course_id": "ENG100",
                    "description": "Enlgish Freshman Composition",
                    "instructor": "Proffesor John Wayne",
                    "grade": "B+"
                },
                {
                    "course_id": "MATH100",
                    "description": "College Algebra",
                    "instructor": "Proffesor Clint Eastwood",
                    "grade": "A-"
                }
            ]
        }
    ]

}

# Bruce Wayne data document 
bruce = {
    "student_id": "1008",
    "first_name": "Bruce",
    "last_name": "Wayne",
    "enrollments": [
        {
            "term": "Summer 2020",
            "gpa": "3.6",
            "start_date": "June 8, 2020",
            "end_date": "August 9, 2020",
            "courses": [
                {
                    "course_id": "GEO100",
                    "description": "Intorduction to Geology",
                    "instructor": "Professor Lee Marvin",
                    "grade": "B"
                },
                {
                    "course_id": "PIANO100",
                    "description": "Introduction to Piano",
                    "instructor": "Proffesor Raquel Welch",
                    "grade": "A+"
                }
            ]
        }
    ]
}

# Gordon Ramsey data document
gordon = {
    "student_id": "1009",
    "first_name": "Gordon",
    "last_name": "Ramsey",
    "enrollments": [
        {
            "term": "Fall 2020",
            "gpa": "2.5",
            "start_date": "August 17, 2020",
            "end_date": "December 20, 2020",
            "courses": [
                {
                    "course_id": "HK100",
                    "description": "Intro to Hell's Kitchen",
                    "instructor": "Professor Martha Steward",
                    "grade": "C+"
                },
                {
                    "course_id": "KITCHEN300",
                    "description": "Advanced Kitchen Cooking",
                    "instructor": "Professor Snoop Dog",
                    "grade": "C+"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements and display output 
print("\n  -- INSERT STATEMENTS --")
wyatt_student_id = students.insert_one(wyatt).inserted_id
print("  Inserted student record Wyatt Earp into the students collection with document_id " + str(wyatt_student_id))

bruce_student_id = students.insert_one(bruce).inserted_id
print("  Inserted student record Bruce Wayne into the students collection with document_id " + str(bruce_student_id))

gordon_student_id = students.insert_one(gordon).inserted_id
print("  Inserted student record Gordon Ramsey into the students collection with document_id " + str(gordon_student_id))