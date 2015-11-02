import dbhandler
from cmd_manager import CommandManager
from pyfilet import Filter


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
def run_mutation_on_file(original_file):
                                                                                                                                         
    #xml_file_list = [(filename, [node, parent ...]), (filename, [node, parent ...])]                                                     
    xml_file_list = xml_mutation.get_xml_file_list(original_file)                                                                         
                                                                                                                                          
    for filename, node_list in xml_file_list:                                                                                             
        #load filename                                                                                                                    
        try:                                                                                                                              
            file = open(filename)                                                                                                         
        except IOError:                                                                                                                   
            print("Error in mainModule: Could not oppen file")                                                                            
            continue #try next filename                                                                                                   
                                                                    
        """                                                                                                                               
        #CommandManager.run fångar felmeddelande från terminalen
        output, error_message = CommandManager.run(Christoffers kod as string)        
        """

        #Om felmeddelande, dvs fel uppkomm -> spara
        if(error_message != ""):            
            #insert to db
            dbhandler.insert(error_message, node_list)


def compilate_with_error_support(filename):
    """
    #fetch felmeddelande
    output, error_message = CommandManager.run(Christoffers kod as string)        
    """    

    print(output)

    #fel uppkom, kolla i db efter matchande fel och returnera nod och snyggt felmdellande
    if(error_message != ""):
        #snygga till felmeddelande
        error_message_pretty = Filter.parse(error_message)
        print("FELMEDDELANDE")
        print(error_message_pretty)

        #hämta nod
        possible_nodes = dbhandler.find(error_message)
        
        print("Following node(s) may be needed:")
        for(node in possible_nodes):
            print(node)

        
