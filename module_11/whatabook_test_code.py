""" 
    what_a_book.py
    Ricardo Guillen Vergara
    5/6/2021
    Console program that interfaces with a MySQL database
"""

""" import statements """
import sys
import csv
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


def what_a_book_website():
   main_menu()


def main_menu():
    print("************Welcome To WhatABook Website**************")
    print()

    choice = (int(input("""

                What Would you Like To Do Today?

                      1: View Books
                      2: View Store Locations
                      3: My Account
                      4: Exit Program

                      Please enter the number located next to your choice: 
                      For example, enter 1 to View Books: """)))

    if choice == 1 :
        view_books()
    elif choice == 2 :
        view_store_locations()
    elif choice == 3:
        my_account()
    elif choice == 4:
        sys.exit(0)
    else:
        print("You must only select numbers 1 thorugh 4")
        print("Please try again")
        main_menu()

def view_books(cursor):
   # inner join query 
    cursor.execute("SELECT book_id, book_name, author, details from book")

    # get the results from the cursor object 
    books = cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    
    # iterate over the player data set and display the results 
    for book in books:
        print(" Book Name: {}".format(book[0]))
        print(" Author: {}".format(book[1]))
        print(" Details: {}".format(books[2]))
        

    
def view_store_locations(cursor):

    cursor.execute("SELECT store_id, locale from store")

    locations = cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")
    
    for location in locations:
        print("  Locale: {}\n".format(location[1]))
   

def my_account():
    """ method to validate users ID """
    
    user_id = input("\nEnter a customer id: For example, enter 1 for user ID 1:   ")

    if user_id >= 0 or user_id <= 3:
        show_account_menu()
    
    else:
        print("Invalid Customer ID Number")
        print("Please try again")
        my_account() 
        
#sys.exit(0)


def show_account_menu():
    
    print("************Welcome To WhatABook Website**************")
    print()

    print("\n  -- Customer Menu --  ")
    choice = (int(input("""

                What Would you Like To Do In Your Account?

                    1: Show My Whishlist
                    2: Show Books to Add to My Whishlist
		            3: Add books to My Wishlist
                    4: Main Menu
                    5: Exit Program

                    Please enter the number located next to your choice: 
                    For example, enter 1 to view your Whishlist 
                                                                      """)))

    if choice == 1 :
        show_whishlist()
    elif choice == 2 :
        show_books_to_add()
    elif choice == 3:
        add_books_to_whishlist()
    elif choice == 4:
        main_menu()
    elif choice == 5:
        sys.exit(0)
    else:
        print("You must only select numbers 1 thorugh 5")
        print("Please try again")
        show_account_menu()

def show_whishlist(cursor, user_id):
    """ query the database for a list of books added to the users wishlist """

    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
    
    wishlist = cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("        Book Name: {}\n".format(book[4]))
        print("        Author: {}\n".format(book[5]))


def show_books_to_add(cursor, user_id):
     pass

def show_books_to_add(cursor, user_id):
     pass

def add_books_to_whishlist():
     pass
    
#the program is initiated, so to speak, here
#main_menu()
what_a_book_website()
