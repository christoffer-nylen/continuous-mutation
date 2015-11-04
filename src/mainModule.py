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

def run_mutation_on_file(original_file):
                                                                                                                                         
    #structure of xml_file_list = [(filename, [node, parent ...]), (filename, [node, parent ...])]                                                     
    mutator = Mutator(original_file)
    xml_file_list = mutator.begin_mutation()
     
    #for test:
    """
    xml_file_list = [("testxml.xml", ["paron/nod1"]), ("paron/testxml_2.xml", ["nod2"]),
                      ("testxml_3.xml", ["nod3"]), ("testxml_4.xml", ["nod4"]),
                      ("testxml_5.xml", ["nod5"])]
    """                                                                                                                                     
    for filename, node_list in xml_file_list:                                                                                             
        #load filename   
        print("FILENAME: " + filename)
        try:  
            xml_file = open(filename)                                                                                                         
        except IOError:                                                                                                                   
            print("Error in mainModule: Could not oppen file")                                                                            
            continue #try next filename                                                                                                   
                                                                    
        
        #CommandManager.run fångar felmeddelande från terminalen
        cmdManger = CommandManager()
        output, error_message = cmdManger.run("g++", filename) #test_execute.executeXML(xml_file))        
        

        #Om felmeddelande, dvs fel uppkomm -> spara
        if(error_message != ""):            
            #insert to db
            print("mainModule.py DB INSERT")
            print("error_msg: " + error_message)
            print("error_type: " + " ".join(node_list))
            dbhandler.insert(error_message, node_list)


def compilate_with_error_support(filename):
    """
    #fetch felmeddelande
    output, error_message = CommandManager.run(Christoffers kod as string)        
    """    

    #print terminal output to help error tracing
    print(output)

    #fel uppkom, kolla i db efter matchande fel och returnera nod och snyggt felmdellande
    if(error_message != ""):
        #snygga till felmeddelande
        error_message_pretty = Filter.parse(error_message)
        print("FELMEDDELANDE")
        print(error_message_pretty)

        #fetch all matching error_message from db
        possible_nodes = dbhandler.find(error_message)
        
        print("Following node(s) may be needed:")
        for node in possible_nodes:
            print(node)

#startup()        
#run_mutation_on_file("lol")
