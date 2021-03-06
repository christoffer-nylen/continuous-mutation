import sqlite3
#re = regexp
import re 
import os.path

"""
SQLite3 implementation module.
Don't call this function directly, use db_handler to interact with database.


tabeler:kolumner
----------------
error_msg: id, felmedelande
error_type: id, typ av fel
errors: fel_id, typ_id
"""


class Database:

    def createDB(self):
        print("CREATE DB")
        cursor = self.cursor

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

        print("DATABASE CREATED")
        
        self.connection.commit()
        
        
    def insert_error_msg(self, error_msg):
        cursor = self.cursor
        
        if(error_msg != "" and error_msg != None):
            cursor.execute("INSERT OR IGNORE INTO error_msg  (msg) VALUES (?)",
                           (error_msg, ))
            self.connection.commit()
            return cursor.lastrowid
        else:
            return None


    def insert_error_type(self, error_types):    
        cursor = self.cursor
            
        #saves node with all parents as an entry
        error_types = "".join(error_types)
        cursor.execute("INSERT OR IGNORE INTO error_type (type) VALUES (?)", (error_types, ))
        
        self.connection.commit()
        return cursor.lastrowid


    def insert_error(self, msg_id, type_id):
        cursor = self.cursor
            
        cursor.execute("INSERT OR IGNORE INTO errors VALUES(?,?)",
                   (msg_id, type_id,))

        self.connection.commit()


    def find(self, _error_msg):
        """
        find error type by error msg. Returns list with all related error types
        [(<error_msg>,<error_type>)]
        """
        cursor = self.cursor
        
        cursor.execute('''SELECT error_msg.msg, error_type.type FROM errors
        LEFT JOIN error_msg
        ON error_msg.id = errors.msg_id
        LEFT JOIN error_type
        ON error_type.id = errors.type_id
        WHERE error_msg.msg LIKE (?)''', ('%'+_error_msg+'%',))
        
        return cursor.fetchall()


    def get_type_id(self, _error_type):
        cursor = self.cursor

        _error_type = "".join(_error_type)
        print("sqlite3_impl.py::get_type_id: " + _error_type)
        cursor.execute('''SELECT id FROM error_type
        WHERE type = (?)''', (_error_type,))
        
        result = cursor.fetchone()
    
        if result is not None:
            return result[0]
        return result
    

    def get_msg_id(self, _error_msg):
        cursor = self.cursor

        cursor.execute('''SELECT id FROM error_msg
        WHERE msg = (?)''', (_error_msg,))

        result = cursor.fetchone()

        if result is not None:
            return result[0]
        return result


    def print_error_msg_table(self):
        cursor = self.cursor

        cursor.execute("SELECT * FROM error_msg")
        
        return cursor.fetchall()


    def print_error_type_table(self):
        cursor = self.cursor

        cursor.execute("SELECT * FROM error_type")
    
        return cursor.fetchall()


    def print_error_table(self):
        cursor = self.cursor

        cursor.execute("SELECT * FROM errors")
    
        return cursor.fetchall()


    def __init__(self, database_name):
        if(re.match("\A[a-zA-Z]+.sql", database_name)):
                                    
            if os.path.isfile(database_name) != True:
                print("DB create new database")
                self.connection = sqlite3.connect(database_name)
                self.cursor = self.connection.cursor()                
                self.createDB()
            else: 
                self.connection = sqlite3.connect(database_name)
                self.cursor = self.connection.cursor()                

                         
        else:
            raise NameError("Error in sqlite3_impl: Database name need to match [a-zA-Z]+.sql")


