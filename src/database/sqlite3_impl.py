import sqlite3

"""
tabeler
id, felmedelande
id, typ av fel
id, filnamn
fel_id, typ_id, fil_id
"""

db = sqlite3.connect(":memory:")

def createDB():
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE error_msg(
    id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, msg TEXT UNIQUE )''')


    cursor.execute('''CREATE TABLE error_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, type TEXT UNIQUE )''')


    cursor.execute('''CREATE TABLE filename(
    id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, name TEXT UNIQUE)''')


    cursor.execute('''CREATE TABLE errors(
    msg_id INT, type_id INT, file_id,
    FOREIGN KEY (msg_id) REFERENCES error_msg(id), 
    FOREIGN KEY (type_id) REFERENCES error_type(id), 
    FOREIGN KEY (file_id) REFERENCES filename(id)
    )''')


    db.commit()

    #db.close()


def insert(error_msg, error_type, filename):
    
    cursor = db.cursor()

    cursor.execute("INSERT OR IGNORE INTO error_msg  (msg) VALUES (?)", (error_msg, ))
    msg_id = cursor.lastrowid;

    cursor.execute("INSERT OR IGNORE INTO error_type (type) VALUES (?)", (error_type, ))
    type_id = cursor.lastrowid;
    
    cursor.execute("INSERT OR IGNORE INTO filename (name) VALUES (?)", (filename,))
    file_id = cursor.lastrowid;

    cursor.execute("INSERT OR IGNORE INTO errors VALUES(?,?,?)", (msg_id, type_id, file_id))

    db.commit()
    #db.close()



def printAllTables():

    cursor = db.cursor()

    print("ERROR_MSG")
    cursor.execute("SELECT * FROM error_msg")
    for row in cursor:
        print(row)

    print("ERROR_TYPE")
    cursor.execute("SELECT * FROM error_type")
    for row in cursor:
        print(row)

    print("FILENAME")
    cursor.execute("SELECT * FROM filename")
    for row in cursor:
        print(row)


    print("ERRORS")
    cursor.execute("SELECT * FROM errors")
    for row in cursor:
        print(row)

        


    
    
createDB()
insert("felmedelane: fel!", "superfeltyp", "felfil.txt")
insert("felmedelane: fel2!", "superfeltyp2", "felfil2.txt")
insert("felmedelane: fel!", "superfeltyp", "felfil3.txt")
printAllTables()
    
    
