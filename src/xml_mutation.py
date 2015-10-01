from xml.dom.minidom import parse, Node

class Mutator:
    def __init__(self, xmlfile):
        self.xmlfile = xmlfile
        self.xmltree = parse(xmlfile)
        self.xmlroot = self.xmltree.documentElement

    def find_nodes(self, node_type):
        node_list = []
        for node in self.xmltree.getElementsByTagName(node_type):
            if node.nodeType == Node.ELEMENT_NODE:
                node_list.append(node)
                print(node)
            if node.hasChildNodes():
                for child in node.childNodes:
                    if child.nodeType == Node.ELEMENT_NODE:
                        node_list.append(child)
                        print(child)

    def remove_node(self, node_type, attribute_name = None):
        # Find nodes matching the searched node type (e.g stub, harness etc)
        for node in self.xmltree.getElementsByTagName(node_type):
            for child in node.childNodes:
                if child.nodeType == Node.ELEMENT_NODE:
                    print("Removing from parent node", child.parentNode.getAttribute("name"),",child", child)
                    child.parentNode.removeChild(child)
            #After all children are removed, remove the node itself
            if node.getAttribute("name") == attribute_name or node.getAttribute("ref") == attribute_name or node.getAttribute("filename_rel") == attribute_name:
                print("Removing from parent node", node.parentNode.tagName,",child", node)
                node.parentNode.removeChild(node)
            

mutator = Mutator("testxml/testconstellations.xml")
print("before removing")
mutator.find_nodes("stub")
mutator.remove_node("csu", "buttons")
print("after removing")
mutator.find_nodes("stub")        
