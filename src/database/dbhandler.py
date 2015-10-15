import sqlite3_impl as DB


def createDB():    
    DB.createDB();
    return "<OK> dbhandler:createDB"
    

def insert_error_msg(error_msg):
    if(error_msg == ""):
        print("<FAILED> in dbhandler:insert_error_msg() invalid in-parameters")
        return "<FAILED>"

    print("<OK> dbhandler:insert_error_msg")
    return DB.insert_error_msg(error_msg)


def insert_error_type(error_type = ""):
    if(error_type == ""):
        print("<FAILED> in dbhandler:insert_error_type() invalid in-parameters")
        return "<FAILED>"

    print("<OK> dbhandler:insert_error_type")
    return DB.insert_error_type(error_type)

def insert_error(msg_id, type_id):
    #implement validation
    return DB.insert_error(msg_id, type_id)

def get_error_msg_id(msg):
   return DB.get_msg_id(msg)


def get_error_type_id(type):
   return DB.get_type_id(type)


def insert(error_msg, error_type):
    """
    insert to sql
    """
    msg_id = get_error_msg_id(error_msg)
    if(msg_id == None):
        msg_id = insert_error_msg(error_msg)
        
    type_id = get_error_type_id(error_type)
    if(type_id == None):
        type_id = insert_error_type(error_type)
    
    if type_id is not None and msg_id is not None:
        insert_error(msg_id, type_id)


def find(error_msg):
    """
    find error type by error message
    """    
    return  DB.find(error_msg)    



