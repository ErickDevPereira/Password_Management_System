import mysql.connector
from hashlib import sha256

#Function that pciks the input mesage and returns as output a mesage with 256 bits in hex given by SHA cryptograph.
def sha_output(msg):
    byte_msg = msg.encode()
    crypto_hex_msg = sha256(byte_msg).hexdigest()
    return crypto_hex_msg
    
#Creating the connection to the server
def connected(host_adress = 'localhost', username = 'root', pw = 'Ichigo007.', db = 'safe_PW'):
    global mydb #Very important to consider the connection as a global scope variable.
    try:
        mydb = mysql.connector.connect(
            host = host_adress,
            user = username,
            password = pw
        )
    except:
        return False
    else:
        cursor = mydb.cursor()
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db}')
        cursor.close()
        mydb.close()
    try:
        mydb = mysql.connector.connect(
            host = host_adress,
            user = username,
            password = pw,
            database = db
        )
    except:
        return False
    else:
        return True

#Creating tables
def create():
    cursor = mydb.cursor()
    sql1 = """CREATE TABLE IF NOT EXISTS Users (
    Id_user INT UNSIGNED AUTO_INCREMENT,
    Username VARCHAR(255) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Phone_number VARCHAR(255) NOT NULL,
    CHECK( EMAIL LIKE '_%@%_.com' ),
    PRIMARY KEY (Id_user)
    )"""
    cursor.execute(sql1)
    cursor.close()
    cursor = mydb.cursor()
    sql2 = """CREATE TABLE IF NOT EXISTS PW_Data (
    Id_record INT UNSIGNED AUTO_INCREMENT,
    Platform VARCHAR(255) NOT NULL,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Id_user INT UNSIGNED, /*id from the logged user that is putting data into the table.*/
    UNIQUE ( Platform, Username, Id_user ), /*Can't reapeat username and platform for the same user*/
    FOREIGN KEY (Id_user) REFERENCES Users(Id_user), /*This FK constraint is important to guarantee data consistency.*/
    PRIMARY KEY (Id_record),
    CHECK ( Platform <> "" AND Username <> "" AND Password <> "")
    )
    """
    cursor.execute(sql2)
    cursor.close()

#function that returns the list of names of the users
def all_users_name():

    cursor = mydb.cursor()
    sql = 'SELECT Username FROM Users'
    cursor.execute(sql)
    registers = cursor.fetchall()
    names = [user[0] for user in registers]
    cursor.close()
    return names
    
#Function that inserts records in the Users table
def insert_user(username, pw, email, phone):

    crypto_pw = sha_output(pw)
    cursor = mydb.cursor()
    sql = 'INSERT INTO Users (Username, Password, Email, Phone_number) VALUES (%s, %s, %s, %s)'
    val = (username, crypto_pw, email, phone)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

#Function that determines if the given login data is present in a record of our table Users
def check_cross_data(username, password):

    crypto_pw = sha_output(password)
    exists = False
    cursor = mydb.cursor()
    sql = 'SELECT Username, Password FROM Users'
    cursor.execute(sql)
    registers = cursor.fetchall()
    for user in registers:
        if username == user[0] and crypto_pw == user[1]:
            exists = True
    cursor.close()
    return exists

#Function that determines if the given user is in the table Users
def check_user(username):

    cursor = mydb.cursor()
    sql = 'SELECT Username FROM Users'
    cursor.execute(sql)
    registers = cursor.fetchall()
    users = [user[0] for user in registers] #List of all names
    if username not in users:
        cursor.close()
        return False
    else:
        cursor.close()
        return True

#Delete data a user from the Users table based on its username
def delete_user(username):
    id = catch_id(username)
    cursor_records = mydb.cursor()
    sql_records = 'DELETE FROM PW_Data WHERE id_user = %s' #The deletion must happen at the Foreign Key column first.
    val_records = (id,)
    cursor_records.execute(sql_records, val_records)
    mydb.commit()
    cursor_user = mydb.cursor()
    sql_user = 'DELETE FROM Users WHERE Username = %s' # After such deletion in the Foreign Key, I can do the deletion in the Primary Key.
    val_user = (username,)
    cursor_user.execute(sql_user, val_user)
    mydb.commit()
    cursor_user.close()
    cursor_records.close()
'''The deletion must happen at the Foreign Key column first.
After such deletion in the Foreign Key, I can do the deletion in the Primary Key.
This order of deletion is very important because SQL forces a FK column to guarantee
data consistency over the referenced PK column'''

#Insert data in the PW_Data for a given user, inserting his id as well
def insert_data(plat, user, pw, id_user):
    #For PW_Data, id_user is the id of the logged user. We have FK at PW_Data.id_user referencing PK at Users.id_user
    cursor = mydb.cursor()
    sql = 'INSERT INTO PW_Data (Platform, Username, Password, Id_user) VALUES (%s, %s, %s, %s)'
    val = (plat, user, pw, id_user)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

#Returns the id of the account with the given username as argument(working with Users table)
def catch_id(username):
    cursor = mydb.cursor()
    sql = 'SELECT Id_user FROM Users WHERE username = %s'
    val = (username,)
    cursor.execute(sql, val)
    id = cursor.fetchall()[0][0]
    cursor.close()
    return id

#Returns the list of tuples of the form (platform, username) for the given id as argument.
def plat_name(id_user):
    cursor = mydb.cursor()
    sql = 'SELECT Platform, Username FROM PW_Data WHERE Id_user = %s'
    val = (id_user,)
    cursor.execute(sql, val)
    results = cursor.fetchall()
    cursor.close()
    return results

#Returns the list of tuples of the form (platform, username, password) for the given user_id as argument
def plat_name_pw(id_user):
    cursor = mydb.cursor()
    sql = 'SELECT Platform, Username, Password FROM PW_Data WHERE Id_user = %s'
    val = (id_user,)
    cursor.execute(sql, val)
    results = cursor.fetchall()
    cursor.close()
    return results

#Function that deletes data for a specific platform and username for an specific user id.
def delete_pw(id_user, platform, username):
    cursor = mydb.cursor()
    sql =  'DELETE FROM PW_Data WHERE Id_user = %s AND Platform = %s AND Username = %s'
    val = (id_user, platform, username)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

#Deletes every data from the PW_Data table for the given the user id.
def delete_all(id_user):
    cursor = mydb.cursor()
    sql = 'DELETE FROM PW_Data WHERE Id_user = %s'
    val = (id_user,)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
