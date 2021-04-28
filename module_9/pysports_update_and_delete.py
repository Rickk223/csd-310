""" 
    pysports_update_and_delete.py
    Ricardo Guillen Vergara
    4/28/2021
    Inserting, updating, and deleting pysports database
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

    # get the cursor object
    cursor = db.cursor()

    # insert a new player record
    cursor.execute("INSERT INTO player(first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1)")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
      

    # show all records in the player table after INSERT
    print("--DISPLAYING PLAYERS AFTER INSERT--")
    
    for player in players:
        print("  Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}\n".format(player[3]))
    
    # UPDATE statement to previously added player
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()

     # show all records in the player table after UPDATE
    print("--DISPLAYING PLAYERS AFTER UPDATE--")
    
    for player in players:
        print("  Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}\n".format(player[3]))
    
    #deleting record
    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()

     # show all records in the player table after DELETE
    print("--DISPLAYING PLAYERS AFTER DELETE--")
    
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