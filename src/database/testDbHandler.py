import dbhandler
import unittest
"""
testing dbhandler.py in database/

"""

class TestCreater(unittest.TestCase):
    

    
    
    def test_insert(self):
        dbhandler.createDB()        
        
        dbhandler.super_insert("felmedelande", "feltyp")
        self.assertEqual(dbhandler.find("felmedelande"),
                    [("felmedelande", "feltyp")])

if __name__ == "__main__":
    unittest.main()

