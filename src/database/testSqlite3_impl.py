import unittest
import sqlite3_impl as db

"""
testing sqlite3_impl.py in database/

"""

class TestCreater(unittest.TestCase):

    

    def test_successful(self):
        db.createDB()    
        error_msg_id = db.insert_error_msg("felmedelane: fel!")
        error_type_id = db.insert_error_type("feltyp")
        db.insert_error(error_msg_id,error_type_id)

        self.assertEqual(db.error_msg_id("felmedelane: fel!"), (1,))
        self.assertEqual(db.error_type_id("feltyp"), (1,))
        self.assertEqual(db.find("felmedelane: fel!"),
                         [("felmedelane: fel!", "feltyp")])
        


        error_msg_id2 = db.insert_error_msg("felmedelane: fel2!")
        error_type_id2 = db.insert_error_type("feltyp2")
        db.insert_error(error_msg_id2,error_type_id2)

        self.assertEqual(db.error_msg_id("felmedelane: fel2!"), (2,))
        self.assertEqual(db.error_type_id("feltyp2"), (2,))
        self.assertEqual(db.find("felmedelane: fel2!"),
                         [("felmedelane: fel2!", "feltyp2")])



        error_msg_id3 = db.insert_error_msg("felmedelane: fel2!")
        error_type_id3 = db.insert_error_type("feltyp3")
        db.insert_error(error_msg_id3,error_type_id3)

        self.assertEqual(db.error_msg_id("felmedelane: fel2!"), (2,))
        self.assertEqual(db.error_type_id("feltyp3"), (3,))
        self.assertEqual(db.find("felmedelane: fel2!"),
                         [("felmedelane: fel2!", "feltyp2"),
                          ("felmedelane: fel2!", "feltyp3")])
                

    def test_failure(self):
        return


    def test_exception(self):
        """
        If no error_msg is recived then error_type
        is matched with all empty error_msg.
        """
        return

    
    
if __name__ == "__main__":
    unittest.main()
