import xml.parsers.expat
from contextlib import contextmanager
from xml.dom.minidom import parse, Node
from xml.dom import NotFoundErr
from datetime import datetime

"""
Class for mutating a given xml file
"""

class Mutator:
    ##
    # @param xmlfile The xml file that is going to be mutated.
    def __init__(self, xmlfile):
        """ 
        Init the Mutator class object
        store a parsed given xml file
        and the root node
        """
        self.xmlfile = xmlfile
        self.init_XML_tree()
        self.xmlfile_node_list = []

    ##
    # @returns An empty list used by other functions.
    def node_list(self):
        """
        Returns an empty list used for helper functions
        """
        node_list = []
        return node_list

    def init_XML_tree(self):
        """
        Generates the xml tree from the xml file.
        """
        try:
            self.xmltree = parse(self.xmlfile)
            self.xmlroot = self.xmltree.documentElement
        except xml.parsers.expat.ExpatError as e:
            return e.arg(0)

    ##
    # @returns A list with all nodes found in the xml tree.
    def find_nodes(self):
        """ 
        Recursivly find all nodes
        """
        return self._find_nodes_helper(self.xmlroot, self.node_list())

    ##
    # @returns A list with all nodes.
    def _find_nodes_helper(self, parent, node_list):
        """
        Helper function that recursivly finds nodes
        """
        for node in parent.childNodes:
            if node.nodeType == node.ELEMENT_NODE:
                node_list.append(node)                               
            self._find_nodes_helper(node, node_list)
        return node_list                

    ##
    # @param node A specified node which a path is generated from.
    # @returns A list with the genareted path to the root node from the specified node.
    def generate_node_path(self, node):
        """ 
        This function generates the node path.
        A list is returned with the node's path to the root node, 
        not including the root.
        """
        try:
            path_to_node = self._generate_node_path_helper(node.parentNode, self.node_list())
            path_to_node.insert(0, self.convert_node_to_string(node))
            return path_to_node
        except ValueError as err:
            print("ERROR:", err)

    ##      
    # @param parent The parent node of the previous node.
    # @param path_to_root_list A list which all nodes from the generated path are saved in.
    # @returns A  list containing all nodes to the root.
    def _generate_node_path_helper(self, parent, path_to_root_list):
        """
        Helper function that builds the path from the node up to the root (not including the root).
        """
        if parent != None and parent != self.xmlroot:
            node_to_string = self.convert_node_to_string(parent)
            path_to_root_list.append(node_to_string)
            self._generate_node_path_helper(parent.parentNode, path_to_root_list)
        return path_to_root_list

    ##
    # @param node A specified node that is converted to the string representation.
    # @returns The string representation of the node.
    def convert_node_to_string(self, node):
        """
        Takes a xml node and returns a string representation of it.
        """
        str_node = node.toxml('utf-8').strip()
        return str_node.decode('utf-8').split(sep='\n')[0]
    ##
    # @param filename The filename that the xml is written to.
    def write(self, filename):
        """
        Write xml to disk.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file_handle:
                self.xmlroot.writexml(file_handle)
        except EnvironmentError as error:
            print(error)
            
                
    def begin_mutation(self):
        """ 
        Mutates a given xml file by removing one node at a time, one after eachother.
        the function yields a touple containing the node affected, a timestamp for the
        modified xml file and the path from the node to the root of the document.
        """
    
        for node in self.find_nodes():
            mutated_node = self.generate_node_path(node)
            filename = mutated_node[0]

            # We need to remove a node and write a new xml file for this specific
            # mutation. Therefore we need to have a reference to a sibling node
            # so that we can insert the node back in its place. This is to not
            # mess with the integrity of the DOM structure for nodes that are to
            # be removed after this one.
            
            sibling = node.nextSibling
            parent = node.parentNode
            parent.removeChild(node)
            self.write(self.xmlfile)
            yield mutated_node
            parent.insertBefore(node, sibling)

        self.write(self.xmlfile)
