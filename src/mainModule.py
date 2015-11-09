#! /usr/bin/env python3

import sys
from database import dbhandler
from command_manager.cmd_manager import CommandManager
from python_filter import pyfilter 
from dummy_classes import test_execute
from xml_mutation.xml_mutation import Mutator
"""
struktur
--------

ladda nodmängd

for

  xml-mutation
  kör xml
  manpiluera felmeddelande
  insert to db

#endfor
"""

def startup():
    dbhandler.createDB();

def run_mutation_on_file(filename):
    mutator = Mutator(filename)
    for node_list in mutator.begin_mutation():

        #CommandManager.run fångar felmeddelande från terminalen
        cmdManger = CommandManager()
        output, error_message = cmdManger.run("g++", filename)

        print("NODELIST: " , node_list)

        #Om felmeddelande, dvs fel uppkomm -> spara
        if(error_message != ""):            
            #insert to db
            print("mainModule.py DB INSERT")
            print("error_msg: " + error_message)
            print("error_type: " + " ".join(node_list))
            dbhandler.insert(error_message, node_list)

if __name__ == "__main__":
    dbhandler.createDB()
    for arg in sys.argv[1:]:
        run_mutation_on_file(arg)
