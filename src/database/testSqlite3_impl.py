import unittest
import sqlite3_impl as db

"""
testing sqlite3_impl.py in database/

"""

class TestCreater(unittest.TestCase):

    

    def test_successful(self):
        db.createDB()    
        db.insert("felmedelane: fel!", "superfeltyp")
        self.assertEqual(db.find("felmedelane: fel!"),
                         [("felmedelane: fel!","superfeltyp")])

        db.insert("felmedelane: fel2", "feltyp2")
        self.assertEqual(db.find("felmedelane: fel2"),
        [("felmedelane: fel2", "feltyp2")])

        db.insert("felmedelane: fel!", "superfeltyp")
        self.assertEqual(db.find("felmedelane: fel!"),
                         [("felmedelane: fel!","superfeltyp")])



    def test_failure(self):
        db.createDB()
        db.insert("felmedelane: fel!", "superfeltyp")
        self.assertNotEqual(db.find("felmedelane: fel!"),
                            [("felmedelane: fel!","")])
        
        db.insert("felmedelane: fel2", "feltyp2")
        self.assertNotEqual(db.find("felmedelane: fel2"),
                            [("felmedelane: fel2", "superfeltyp")])
        

    def test_exception(self):
        """
        If no error_msg is recived then error_type
        is matched with all empty error_msg.
        """

        db.createDB()
        db.insert("", "feltyp3")
        self.assertEqual(db.find(""),
                            [("", "feltyp3")])
       
        db.insert("", "feltyp4")
        self.assertEqual(db.find(""),
                            [("", "feltyp4")])
        


    
    
if __name__ == "__main__":
    unittest.main()
