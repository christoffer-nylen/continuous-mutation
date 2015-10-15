from xml.dom.minidom import parse, Node
from xml.dom import NotFoundErr
import time

class Mutator:
    def __init__(self, xmlfile):
        """ 
        Init the Mutator class object
        store a parsed given xml file
        store linenumbers and the root node
        """
        self.xmlfile = xmlfile
        self.xmltree = parse(xmlfile)
        self.xmlroot = self.xmltree.documentElement
        self.xmlfile_lines_modified = []
        self.xmlfile_linenumbers = {}
        self.xmlfile_get_linenumbers(xmlfile)

    def NodeList(self):
        """Returns an empty list used for helper functions"""
        node_list = []
        return node_list

    def find_nodes(self, node_type, node_attribute = None):
        """ Recursivly locate a given node by its tag name and (optional) node_attribute """
        return self._find_nodes_helper(self.xmlroot, node_type, node_attribute, self.NodeList())

    def _find_nodes_helper(self, parent, name, attribute, node_list):
        """
        Helper function that recursivly finds a node, given a name and/or attribute
        """
        for node in parent.childNodes:
            if node.nodeType == node.ELEMENT_NODE:
                if node.tagName == name and attribute in \
                                dict(node.attributes.items()).values():
                    node_list.append(node)
                elif node.tagName == name and attribute == None:
                    node_list.append(node)
            self._find_nodes_helper(node, name, attribute, node_list)
        return node_list                

    def remove_node(self, node_type, attribute_name = None):
        """
        Remove a node matching the node_type, the optional attribute_name can be provided to narrow down possible candidates for the removal
        """
        nodes_for_removal = self.find_nodes(node_type, attribute_name)
        if nodes_for_removal:
            for node in nodes_for_removal:
                try:
                    self.xmlfile_lines_modified.append(str(self.xmlfile_linenumbers[self.convert_node_to_string(node)]))
                    sibling = node.previousSibling
                    node.parentNode.removeChild(node)
                    sibling.nodeValue = sibling.nodeValue.strip()
                except ValueError as err:
                    print("ERROR:", err)

    def convert_node_to_string(self, node):
        """
        Takes a xml node and returns a string representation of it
        """
        str_node = node.toxml('utf-8').strip()
        return str_node.decode('utf-8').split(sep='\n')[0]

    def remove_attribute(self, node, name):
        """
        Remove an attribute specified by name from a given node
        """
        try:
            node.removeAttribute(name)
        except NotFoundErr:
            print("ERROR: Attribute not found.")
        except AttributeError as err:
            print("ERROR:", err)

    def xmlfile_get_linenumbers(self, filename):
        """
        Sequentially read through the file storing each row tied with its linenumber
        """
        with open(filename, "r") as xmlfile:
            for linenumber, line in enumerate(xmlfile):
                self.xmlfile_linenumbers[line.strip()] = linenumber+1

    def generate_filename(self):
        """ 
        Generate a filename for a modified xml.
        The filename will consist of a timestamp and the lines that have been modified, in order
        """
        lines_modified = ','.join(self.xmlfile_lines_modified)
        timestamp = time.strftime("%Y-%m-%d-%H:%M:%S")
        file_type = ".xml"
        file_name = "{0}-lines_changed:{1}{2}".format(timestamp, lines_modified, file_type)
        return file_name
            
    def write(self):
        """
        Write xml to disk using a generated filename
        """
        with open(self.generate_filename(), 'w', encoding='utf-8') as file_handle:
            self.xmlroot.writexml(file_handle)

mutator = Mutator("testxml/testconstellations.xml")
found = mutator.find_nodes("stub", "statistics")
mutator.remove_attribute(found[0], "asdfa")
print(found)
mutator.remove_node("stub", "control_unit")
mutator.write()
