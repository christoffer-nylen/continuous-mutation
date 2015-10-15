from xml.dom.minidom import parse, Node
from xml.dom import NotFoundErr
from datetime import datetime

class Mutator:
    def __init__(self, xmlfile):
        """ 
        Init the Mutator class object
        store a parsed given xml file
        store linenumbers and the root node
        """
        self.xmlfile = xmlfile
        self.initXMLTree()
        self.xmlfile_node_list = []
            
    def NodeList(self):
        """Returns an empty list used for helper functions"""
        node_list = []
        return node_list

    def initXMLTree(self):
        self.xmltree = parse(self.xmlfile)
        self.xmlroot = self.xmltree.documentElement
    
    def find_nodes(self, node_type = None, node_attribute = None):
        """ Recursivly locate a given node by its tag name and (optional) node_attribute """
        return self._find_nodes_helper(self.xmlroot, self.NodeList(), node_type, node_attribute)

    def _find_nodes_helper(self, parent, node_list, name = None, attribute = None):
        """
        Helper function that recursivly finds a node, given a name and/or attribute
        """
        for node in parent.childNodes:
            if node.nodeType == node.ELEMENT_NODE:
                if name != None or attribute != None:
                    if node.tagName == name and attribute in \
                       dict(node.attributes.items()).values():
                        node_list.append(node)
                    elif node.tagName == name and attribute == None:
                        node_list.append(node)
                else:
                    node_list.append(node)                               
            self._find_nodes_helper(node, node_list, name, attribute)
        return node_list                

    def remove_node(self, node):
        try:
            print(node)
            path_to_removed_node = self._remove_node_helper(node.parentNode, self.NodeList())
            path_to_removed_node.insert(0, node) # insert the removed node first in the path_to_removed_node list
            generated_filename = self.generate_filename()
            tuple_removed_node_context = (generated_filename, path_to_removed_node)
            return tuple_removed_node_context
        except ValueError as err:
            print("ERROR:", err)
          
            
    def _remove_node_helper(self, parent, path_to_root_list):
        """
        Helper function that builds the path from the node to be removed up to the root.
        This gives crucial information about the affected node and its context.
        """
        if parent != None:
                path_to_root_list.append(parent)
                self._remove_node_helper(parent.parentNode, path_to_root_list)
        return path_to_root_list
        
    
    def remove_specified_node(self, node_type = None, attribute_name = None):
        """
        Remove a node matching the node_type, the optional attribute_name can be provided to narrow down possible candidates for the removal
        """
        nodes_for_removal = self.find_nodes(node_type, attribute_name)
        if nodes_for_removal:
            for node in nodes_for_removal:
                try:
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

    def remove_specified_attribute(self, node, name):
        """
        Remove an attribute specified by name from a given node
        """
        try:
            node.removeAttribute(name)
        except NotFoundErr:
            print("ERROR: Attribute not found.")
        except AttributeError as err:
            print("ERROR:", err)

    def generate_filename(self):
        """ 
        Generate a filename for a modified xml.
        The filename will consist of a timestamp and the lines that have been modified, in order
        """
        time = datetime.now()
        timestamp = time.strftime("%H:%M:%S.%f")
        file_type = ".xml"
        file_name = "{0}{1}".format(timestamp, file_type)
        return file_name
            
    def write(self, filename):
        """
        Write xml to disk using a generated filename
        """
        with open(filename, 'w', encoding='utf-8') as file_handle:
            self.xmlroot.writexml(file_handle)

    def begin_mutation(self):
        mutated_nodes = []
        for node in self.find_nodes():
            mutated_node = self.remove_node(node)
            filename = mutated_node[0] # first tuple index is the filename
            #self.write(filename)
            mutated_nodes.append(mutated_node)
            print("Removing from:", node.parentNode, " child:", node)
            node.parentNode.removeChild(node)
            self.initXMLTree()
        return mutated_nodes
    
mutator = Mutator("testxml/testconstellations.xml")
return_list = mutator.begin_mutation()
for touple in return_list:
    print(touple)

""" Because we remove a node each time, there will be fewer parentNodes to traverse, this results in
a behaviour we dont want. Going recursivly upwards from a node to its root will not work unless
we can find some way to re-parse the whole tree structure i.e "restoring" the tree after each removal so that we can continue removing one node at a time. I have tried to do this but i believe the "old" DOM structure is still used although i try to re-initialize the tree." Doing downward recursion might solve the issue. Or atleast i think so."
