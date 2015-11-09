from database import dbhandler
from command_manager.cmd_manager import CommandManager
from python_filter.pyfilter import Filter 
from dummy_classes import test_execute
from xml_mutation.xml_mutation import Mutator
"""
struktur
--------

ladda nodmängd

for nod in xml-mutation
  kör xml
  manpiluera felmeddelande
  insert to db

#endfor
"""


def startup():
    #drop and create tables needed for saving errors
    dbhandler.createDB();

    ##
    # @param filename the xml file to mutate on 
    # @returns void
def run_mutation_on_file(filename):
    """
    filename is the xml file for generation make files.
    This function mutate on the file so that one node
    is missing per iteration. After mutating so every 
    node have once been remove the original file will 
    be restored.

    In every iteration the usuall procedure for creating
    makefiles is executed. If any errors occures during
    the "make" command the function[run_mutation_on_file]
    will save the error message and the node with all its
    parent nodes saved into tables in the (sqlite3)database. 
    """
    print("run mutation on", filename)
    mutator = Mutator(filename)
    prettyFilter = Filter()
    for node_list in mutator.begin_mutation():
        try:
            print("NODELIST: " , node_list)
            #CommandManager.run catch error_messages
            cmdManager = CommandManager()
            output, error_message = cmdManger.run("g++", filename)

            """
            Insert procedure for generating and building makefiles
            here. Use cmdManager.run([command]...,) 
            example: cmdManager.run("mbede-generator", "-l")
            example: cmdManager.run("mv", filename, "new_filename.txt")

            When runing "make" command use the vars output and error_message
            to make it possible to save content to database.
            """

            """
            #example of build procedure code
            cmdManager.run("mbede-generator", "-l")
            cmdManager.run("make", "makefiles")
            output, error_message = cmdaManger.run("make")#, target)
            """
        
            #If error occures saved the errmsg in db
            if(error_message != ""):            
                
                error_message_pretty = prettyFilter.parse(error_message) 
                #reverse order of nodes. Parent... node
                node_list = node_list[::-1]

                print("mainModule.py DB INSERT")
                print("error_msg: " + error_message_pretty)
                print("error_type: " + " ".join(node_list)

                dbhandler.insert(error_message_pretty, node_list)

        except:
            #if something goes wrong continue to next mutation
            continue
            

#startup()
#run_mutation_on_file("dummy_classes/testxml.xml")
