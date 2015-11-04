import unittest
from xml_mutation import Mutator
import xml.dom

class XmlMutationTests(unittest.TestCase):

    def setUp(self):
        self.mutator = Mutator("../testxml/testconstellations.xml")

    def tearDown(self):
        self.mutator = None

    def test_find_node(self):
        found = self.mutator.find_nodes("stub", "statistics")
        self.assertEqual('<stub name="statistics"/>', found[0].toxml())

    def test_remove_node(self):
        self.mutator.remove_node("stub", "control_unit")
        found = self.mutator.find_nodes("stub", "control_unit")
        self.assertEqual(len(found), 0)

    def test_remove_attribute(self):
        found = self.mutator.find_nodes("regression_type", "integration")
        self.mutator.remove_attribute(found[0], "integration")
        #print("ARGS:", self.mutator.remove_attribute(found[0], "integration").args)
        self.assertEqual(self.mutator.remove_attribute(found[0], "integration").code, xml.dom.NOT_FOUND_ERR)

    def test_remove_non_existing_attribute(self):
        found = self.mutator.find_nodes("lib", "text")
        self.assertEqual(len(found), 1)
        self.assertEqual(self.mutator.remove_attribute(found[0], "doesNotExist").code, xml.dom.NOT_FOUND_ERR)
    

if __name__ == '__main__':
    unittest.main()
