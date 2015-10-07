import sqlite3_impl as DB


def createDB():
    DB.createDB();
    return "<OK> dbhandler:createDB"

def insert(error_msg, error_type):
    if(error_msg == "" or error_type == ""):
        return "<FAILED> in dbhandler:insert() not enought parameters";

    print("<OK> dbhandler:insert")
    return DB.insert(error_msg, error_type)


def find(error_msg):
    if(error_msg == ""):
        return "<FAILED> in dbhandler:find() not enought parameters";

    print ("<OK> dbhandler:find()")    
    return DB.find(error_msg)



