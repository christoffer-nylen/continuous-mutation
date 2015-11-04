from xml.dom.minidom import parse, Node
from xml.dom import NotFoundErr
from datetime import datetime

class Mutator:
    def __init__(self, xmlfile):
        """ 
        Init the Mutator class object
        store a parsed given xml file
        and the root node
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
    
    def find_nodes(self):
        """ Recursivly find all nodes"""
        return self._find_nodes_helper(self.xmlroot, self.NodeList())

    def _find_nodes_helper(self, parent, node_list):
        """
        Helper function that recursivly finds nodes
        """
        for node in parent.childNodes:
            if node.nodeType == node.ELEMENT_NODE:
                node_list.append(node)                               
            self._find_nodes_helper(node, node_list)
        return node_list                

    def generate_node_path(self, node):
        """ This function generates the node path.
        A tuple is returned with a generated filename and the node together with its path to the root.
        """
        try:
            path_to_node = self._generate_node_path_helper(node.parentNode, self.NodeList())
            path_to_node.insert(0, self.convert_node_to_string(node))
            generated_filename = self.generate_filename()
            tuple_node_context = (generated_filename, path_to_node)
            return tuple_node_context
        except ValueError as err:
            print("ERROR:", err)
          
            
    def _generate_node_path_helper(self, parent, path_to_root_list):
        """
        Helper function that builds the path from the node up to the root (not including the root).
        """
        if parent != None and parent != self.xmlroot:
            node_to_string = self.convert_node_to_string(parent)
            path_to_root_list.append(node_to_string)
            self._generate_node_path_helper(parent.parentNode, path_to_root_list)
        return path_to_root_list
        
    def convert_node_to_string(self, node):
        """
        Takes a xml node and returns a string representation of it.
        """
        str_node = node.toxml('utf-8').strip()
        return str_node.decode('utf-8').split(sep='\n')[0]

    def generate_filename(self):
        """ 
        Generate a filename for a modified xml.
        """
        time = datetime.now()
        timestamp = time.strftime("%H:%M:%S.%f")
        file_type = ".xml"
        file_name = "{0}{1}".format(timestamp, file_type)
        return file_name

    def write(self, filename):
        """
        Write xml to disk.
        """
        with open(filename, 'w', encoding='utf-8') as file_handle:
            self.xmlroot.writexml(file_handle)

    def begin_mutation(self):
        """ Mutates a given xml file by removing one node at a time, one after eachother.
        the function returns a list containing the node affected, a timestamp for the modified xml file and the path
        from the node to the root of the document. """
        mutated_nodes = []
        for node in self.find_nodes():
            mutated_node = self.generate_node_path(node)
            filename = mutated_node[0]
            mutated_nodes.append(mutated_node)

            # We need to remove a node and write a new xml file for this specific
            # mutation. Therefore we need to have a reference to a sibling node
            # so that we can insert the node back in its place. This is to not
            # mess with the integrity of the DOM structure for nodes that are to
            # be removed after this one.
            
            sibling = node.nextSibling
            parent = node.parentNode
            parent.removeChild(node)

            self.write(filename)
            
            parent.insertBefore(node, sibling)
        return mutated_nodes
