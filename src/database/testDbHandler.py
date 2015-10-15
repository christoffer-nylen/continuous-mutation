import dbhandler
import unittest
"""
testing dbhandler.py in database/

"""

class TestCreater(unittest.TestCase):
    

    
    
    def test_insert(self):
        dbhandler.createDB()        
        
        dbhandler.insert("felmeddelande", "feltyp")

        self.assertEqual(dbhandler.get_error_msg_id("felmeddelande"), 1)
        self.assertEqual(dbhandler.get_error_type_id("feltyp"), 1)

        self.assertEqual(dbhandler.find("felmeddelande"),
                    [("felmeddelande", "feltyp")])


        dbhandler.insert("felmeddelande2", "feltyp2")

        self.assertEqual(dbhandler.get_error_msg_id("felmeddelande2"), 2)
        self.assertEqual(dbhandler.get_error_type_id("feltyp2"), 2)

        self.assertEqual(dbhandler.find("felmeddelande2"),
                    [("felmeddelande2", "feltyp2")])



        dbhandler.insert("felmeddelande", "feltyp")

        self.assertEqual(dbhandler.get_error_msg_id("felmeddelande"), 1)
        self.assertEqual(dbhandler.get_error_type_id("feltyp"), 1)

        self.assertEqual(dbhandler.find("felmeddelande"),
                    [("felmeddelande", "feltyp")])



        dbhandler.insert("felmeddelande3", "feltyp")

        self.assertEqual(dbhandler.get_error_msg_id("felmeddelande3"), 3)
        self.assertEqual(dbhandler.get_error_type_id("feltyp"), 1)

        self.assertEqual(dbhandler.find("felmeddelande3"),
                    [("felmeddelande3", "feltyp")])


        dbhandler.insert("felmeddelande3", "feltyp3")

        self.assertEqual(dbhandler.get_error_msg_id("felmeddelande3"), 3)
        self.assertEqual(dbhandler.get_error_type_id("feltyp3"), 3)

        self.assertEqual(dbhandler.find("felmeddelande3"),
                    [ ("felmeddelande3", "feltyp"), ("felmeddelande3", "feltyp3")])


if __name__ == "__main__":
    unittest.main()

