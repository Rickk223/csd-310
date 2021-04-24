""" 
    pysports_queries.py
    Ricardo Guillen Vergara
    4/24/2021
    Program to query the team and player tables 
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # select query for team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # get the results from the cursor object 
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # for loop to get the theam's data to teh screen
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # query for the player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # for loop to get player data to the screen
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    
    db.close()