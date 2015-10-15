import dbhandler
from cmd_manager import CommandManager


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
        #fetch felmeddelande
        felmeddelande = CommandManager.run(Christoffers kod as string)        
"""

#snygga till felmeddelande

        #insert to db
        dbhandler.insert()
