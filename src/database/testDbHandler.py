import dbhandler
import unittest
"""
testing dbhandler.py in database/

"""

class TestCreater(unittest.TestCase):
    

    

    def test_insert(self):
        #sucesstest
        dbhandler.createDB()    
        
        dbhandler.insert("felmedelane: fel!", "superfeltyp")
        self.assertEqual(dbhandler.find("felmedelane: fel!"),
                         [("felmedelane: fel!","superfeltyp")])

        #exception

        self.assertEqual(dbhandler.insert("", "superfeltyp"),
                         "<FAILED> in dbhandler:insert() not enought parameters")

        self.assertEqual(dbhandler.insert("felmedelande", ""),
                         "<FAILED> in dbhandler:insert() not enought parameters")
        
        self.assertEqual(dbhandler.insert("", ""),
                         "<FAILED> in dbhandler:insert() not enought parameters")


    
    
if __name__ == "__main__":
    unittest.main()

