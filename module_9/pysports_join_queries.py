""" 
    Title: pysports_join_queries.py
    Ricardo Guillen Vergara
    4/28/2021
    Inner Join for player and team tables
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

    # inner join for player and team by team_id
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #this statement gets the results from the cursor object declared above
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    # for loop to display all records in the query and properly formated  
    for player in players:
        print("  Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}\n".format(player[3]))

    

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