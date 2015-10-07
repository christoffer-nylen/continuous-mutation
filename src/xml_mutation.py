from xml.dom.minidom import parse, Node
from xml.dom import NotFoundErr
import time

class Mutator:
    def __init__(self, xmlfile):
        """ Init the class objects parses an xml file and stores the root node"""
        self.xmlfile = xmlfile
        self.xmltree = parse(xmlfile)
        self.xmlroot = self.xmltree.documentElement
        self.modified_lines = []
        self.linenumbers = {}
        self.store_linenumbers(xmlfile)

    def NodeList(self):
        """Returns an empty list used for helper functions"""
        node_list = []
        return node_list

    def find_nodes(self, node_type, node_attribute = None):
        """ Recursivly locate a given node by its tag name and (optional) node_attribute """
        return self._find_nodes_helper(self.xmlroot, node_type, node_attribute, self.NodeList())

    def _find_nodes_helper(self, parent, name, attribute, node_list):
        """ Helper function that recursivly finds a node, given a name and/or attribute """
        for node in parent.childNodes:
            #print(node)
            if node.nodeType == node.ELEMENT_NODE:
                if node.tagName == name and attribute in \
                                dict(node.attributes.items()).values():
                    node_list.append(node)
                elif node.tagName == name and attribute == None:
                    node_list.append(node)
            self._find_nodes_helper(node, name, attribute, node_list)
        return node_list                

    def remove_node(self, node_type, attribute_name = None):
        found = self.find_nodes(node_type, attribute_name)
        if found:
            for node in found:
                try:
                    self.modified_lines.append(str(self.linenumbers[self.convert_node_to_string(node)]))
                    sibling = node.previousSibling
                    node.parentNode.removeChild(node)
                    sibling.nodeValue = sibling.nodeValue.strip()
                except ValueError as err:
                    print("ERROR:", err)

    def convert_node_to_string(self, node):
        str_node = node.toxml('utf-8').strip()
        return str_node.decode('utf-8').split(sep='\n')[0]

    def remove_attribute(self, node, name):
        try:
            node.removeAttribute(name)
        except NotFoundErr:
            print("ERROR: Attribute not found.")
        except AttributeError as err:
            print("ERROR:", err)

    def store_linenumbers(self, filename):
        with open(filename, "r") as xmlfile:
            for linenumber, line in enumerate(xmlfile):
                self.linenumbers[line.strip()] = linenumber+1

    def generate_filename(self):
        lines = ','.join(self.modified_lines)
        file_name = time.strftime("%Y-%m-%d-%H:%M:%S") + "-lines_changed:" + lines
        print("FILENAME: ", file_name)
        return file_name
            
    def write(self):
        with open(self.generate_filename(), 'w', encoding='utf-8') as file_handle:
            self.xmlroot.writexml(file_handle)

mutator = Mutator("testxml/testconstellations.xml")
found = mutator.find_nodes("stub", "statistics")
mutator.remove_attribute(found, "asdfa")
print(found)
mutator.remove_node("stub", "control_unit")
mutator.write()
