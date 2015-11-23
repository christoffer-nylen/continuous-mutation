from database.sqlite3_impl import Database

"""
Middlehand for sql commands.
Relevant function: insert, find
See functions for more info
"""

class DatabaseHandler:

    def __init__(self,database_name):
        self.db = Database(database_name)
        print("<OK> dbhandler:createDB")


    def insert_error_msg(self, error_msg):
        if error_msg == "":
            print("<FAILED> in dbhandler:insert_error_msg() invalid in-parameters")
            return "<FAILED>"

        print("<OK> dbhandler:insert_error_msg")
        return self.db.insert_error_msg(error_msg)


    def insert_error_type(self, error_type):
        if error_type == "":
            print("<FAILED> in dbhandler:insert_error_type() invalid"
                  "in-parameters")
            return "<FAILED>"

        print("<OK> dbhandler:insert_error_type")
        return self.db.insert_error_type(error_type)


    def insert_error(self, msg_id, type_id):
        # Implement validation
        return self.insert_error(msg_id, type_id)


    def get_error_msg_id(self,msg):
        return self.db.get_msg_id(msg)


    def get_error_type_id(self, type):
        return self.db.get_type_id(type)


    def insert(self, error_msg, error_type):
        """
        insert to sql if not exists.
        Connect error_msg and error_type in errors tabel if relation not already
        exists
        """
        msg_id = self.db.get_msg_id(error_msg)
        if msg_id is None:
            msg_id = self.db.insert_error_msg(error_msg)
            
        type_id = self.db.get_type_id(error_type)
        if type_id is None:
            type_id = self.db.insert_error_type(error_type)
                
        if type_id is not None and msg_id is not None:
            self.db.insert_error(msg_id, type_id)


    def find(self,error_msg):
        """
        find error type by error message
        """    
        return self.db.find(error_msg)    

    def print_all_tables(self):
        print(self.db.print_error_msg_table())
        print(self.db.print_error_type_table())
        print(self.db.print_error_table())


    def print_msg_table(self):
        return(self.db.print_error_msg_table())

    def print_type_table(self):
        return(self.db.print_error_type_table())

    def print_error_table(self):
        return(self.db.print_error_table())
