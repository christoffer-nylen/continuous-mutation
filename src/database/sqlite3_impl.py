import sqlite3


"""
tabeler:kolumner
----------------
error_msg: id, felmedelande
error_type: id, typ av fel
errors: fel_id, typ_id
"""

db = sqlite3.connect(":memory:")

def createDB():
    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS error_msg")
    cursor.execute("DROP TABLE IF EXISTS error_type")
    cursor.execute("DROP TABLE IF EXISTS errors")


    cursor.execute('''CREATE TABLE error_msg(
    id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, msg TEXT UNIQUE )''')


    cursor.execute('''CREATE TABLE error_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, type TEXT UNIQUE )''')


    cursor.execute('''CREATE TABLE errors(
    msg_id INT, type_id INT,
    FOREIGN KEY (msg_id) REFERENCES error_msg(id), 
    FOREIGN KEY (type_id) REFERENCES error_type(id),
    PRIMARY KEY (msg_id, type_id))''')


    db.commit()

    #db.close()

def insert_error_msg(error_msg):
    cursor = db.cursor()

    cursor.execute("INSERT OR IGNORE INTO error_msg  (msg) VALUES (?)", (error_msg, ))
    #msg_id = cursor.lastrowid;
    db.commit()
    return cursor.lastrowid; #return msg_id

def insert_error_type(error_type):    
    cursor = db.cursor()

    cursor.execute("INSERT OR IGNORE INTO error_type (type) VALUES (?)", (error_type, ))

        
    db.commit()
    return cursor.lastrowid #retunrn type_id
    
def insert_error(msg_id, type_id):
    cursor = db.cursor()
    
    cursor.execute("INSERT OR IGNORE INTO errors VALUES(?,?)", (msg_id, type_id,))
    
    db.commit()

   

def find(_error_msg):
    """
    find error type by error msg. Returns list with all related error types
    [(<error_msg>,<error_type>)]
    """
    cursor = db.cursor()

    cursor.execute('''SELECT error_msg.msg, error_type.type FROM errors
    LEFT JOIN error_msg
    ON error_msg.id = errors.msg_id
    LEFT JOIN error_type
    ON error_type.id = errors.type_id
    WHERE error_msg.msg = (?)''', (_error_msg,))

    return cursor.fetchall()


def get_type_id(_error_type):
    cursor = db.cursor()

    cursor.execute('''SELECT id FROM error_type
    WHERE type = (?)''', (_error_type,))

    result  = cursor.fetchone()

    if result is not None:
        return result[0]
    return result

def get_msg_id(_error_msg):
    cursor = db.cursor()
    
    cursor.execute('''SELECT id FROM error_msg
    WHERE msg = (?)''', (_error_msg,))

    result  = cursor.fetchone()

    if result is not None:
        return result[0]
    return result
