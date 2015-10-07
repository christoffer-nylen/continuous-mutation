import unittest
import sqlite3_impl as db

"""
testing sqlite3_impl.py in database/

"""

class TestCreater(unittest.TestCase):

    def test_successful(self):
        db.createDB()
        db.insert("felmedelane: fel!", "superfeltyp", "felfil.txt")
        self.assertEqual(db.find("felmedelane: fel!"),
                         [("felmedelane: fel!","superfeltyp")])

        db.insert("felmedelane: fel2", "feltyp2", "felfil.txt")
        self.assertEqual(db.find("felmedelane: fel2"),
        [("felmedelane: fel2", "feltyp2")])

        db.insert("felmedelane: fel!", "superfeltyp", "felfil.txt")
        self.assertEqual(db.find("felmedelane: fel!"),
                         [("felmedelane: fel!","superfeltyp")])



    
if __name__ == "__main__":
    unittest.main()
