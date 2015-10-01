from xml.dom.minidom import parse, Node

class Mutator:
    def __init__(self, xmlfile):
        """ Init the class objects parses an xml file and stores the root node"""
        self.xmlfile = xmlfile
        self.xmltree = parse(xmlfile)
        self.xmlroot = self.xmltree.documentElement

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
                node.parentNode.removeChild(node)

    def write(self, file_name):
        file_handle = open(file_name, 'wb')
        self.xmlroot.writexml(file_handle)
        file_handle.close()

mutator = Mutator("testxml/testconstellations.xml")
found = mutator.find_nodes("stub", "control_unit")
print(found)
mutator.remove_node("stub", "control_unit")
mutator.write("test.xml")
