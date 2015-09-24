from xml.dom.minidom import parse, Node

class Mutator:
    def __init__(self, xmlfile):
        self.xmlfile = xmlfile
        self.xmltree = parse(xmlfile)

    def find_nodes(self, node_type):
        node_list = []
        for node in self.xmltree.getElementsByTagName(node_type):
            node_list.append(node)
            print(node.getAttribute("name"))

    def remove_node(self, node_type, node_name):
        for node in self.xmltree.getElementsByTagName(node_type):
            if node.childNodes is not None:
                for children in node.getChildren:
                    if node.getAttribute(node_name):
                        xmltree.documentElement.removeChild(node)
            else:
                xmltree.documentElement.removeChild(node)
            
        
mutator = Mutator("testconstellations.xml")
mutator.find_nodes("stub")
mutator.remove_node("stub", "hardware_layer")
mutator.find_nodes("stub")        
