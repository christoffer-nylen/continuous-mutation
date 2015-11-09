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
    dbhandler.createDB();

def run_mutation_on_file(filename):
    print("run mutation on", filename)
    mutator = Mutator(filename)
    prettyFilter = Filter()
    for node_list in mutator.begin_mutation():
        try:
            print("NODELIST: " , node_list)
            #CommandManager.run fångar felmeddelande från terminalen
            cmdManger = CommandManager()
            output, error_message = cmdManger.run("g++", filename)
            """
            cmdManger.run("mbede-generator", "-l")
            cmdManger.run("make", "makefiles")
            output, error_message = cmdManger.run("make")#, target)
            """
        
            #Om felmeddelande, dvs fel uppkomm -> spara
            if(error_message != ""):            
                #insert to db
                print("mainModule.py DB INSERT")
                print("error_msg: " + error_message)
                print("error_type: " + " ".join(node_list))
                error_message_pretty = prettyFilter.parse(error_message) 
                #reverse order of nodes. Parent...node
                node_list = node_list[::-1]
                dbhandler.insert(error_message_pretty, node_list)

        except:
            #if something goes wrong continue to next mutation
            continue
            

startup()
run_mutation_on_file("dummy_classes/testxml.xml")
