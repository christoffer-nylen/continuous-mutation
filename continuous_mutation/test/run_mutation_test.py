import unittest
import continuous_mutation.xml_mutation.run_mutator as run_mutator
from continuous_mutation.database import dbhandler

class TestCreater(unittest.TestCase):

    def run(self):

        #drop and create db
        run_mutator.startup()

        run_mutator.run_mutation_on_file("dummy_classes/testxml.xml")
        print("test")
        print(dbhandler.print_all_tables())

        self.assertEqual(dbhandler.print_error_table(),
[(1, '<testconstellation name="user_interface_test">'),
 (2, '<regression_type name="integration"/>'),
 (4, '<tested_object>      '),
 (6, '<test ref="Feline.cc"/>'),
 (9, '<test ref="Animal.cc"/>'),
 (12, '<harness>'),
 (14, '<test ref="Canine.cc"/>'),
 (17, '<test ref="Dog.cc"/>'),
 (20, '<test ref="Cat.cc">'),
 (23, '<test ref="Lion.cc"/>')]
)


if __name__ == "__main__":
    unittest.main()
