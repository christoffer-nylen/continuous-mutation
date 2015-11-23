import unittest
from continuous_mutation.xml_mutation.xml_mutator import Mutator
import xml.dom

class XmlMutationTests(unittest.TestCase):

    def setUp(self):
        self.mutator = Mutator("../xml_mutation/testxml/testconstellations.xml")

    def tearDown(self):
        self.mutator = None

    def test_node_list(self):
        list = self.mutator.node_list()
        self.assertEqual(0, len(list))
    
    def test_find_nodes(self):
        all_nodes = self.mutator.find_nodes()
        self.assertEqual('<testconstellation name="user_interface_test">', self.mutator.convert_node_to_string(all_nodes[0]))
    
    def test_generate_node_path(self):
        all_nodes = self.mutator.find_nodes()
        node_path = self.mutator.generate_node_path(all_nodes[2])
        self.assertEqual(self.mutator.convert_node_to_string(all_nodes[2]), node_path[0])
        self.assertEqual(self.mutator.convert_node_to_string(all_nodes[0]), node_path[len(node_path)-1])
        
    def test_convert_node_to_string(self):
        all_nodes = self.mutator.find_nodes()
        str_node = self.mutator.convert_node_to_string(all_nodes[0])
        self.assertEqual('<testconstellation name="user_interface_test">', self.mutator.convert_node_to_string(all_nodes[0]))

    def test_begin_mutation(self):
        all_nodes = self.mutator.find_nodes()
        for index, mutated_node in enumerate(self.mutator.begin_mutation()):
            self.assertEqual(self.mutator.convert_node_to_string(all_nodes[index]), mutated_node[0])
        
    
if __name__ == '__main__':
    unittest.main()

