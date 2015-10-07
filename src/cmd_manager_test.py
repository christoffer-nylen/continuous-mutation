import unittest
from cmd_manager import CommandManager

class TestCmdManager(unittest.TestCase):

    def testOutput(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("printf", "Test")
        self.assertEqual(errors, "")
        self.assertEqual(output, "Test")

    def testError(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("printf")
        self.assertEqual(output, "")
        self.assertTrue(len(errors) > 0)

    def testScript(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("python3", "cmd_manager.py")
        self.assertEqual(output, "stdout")
        self.assertEqual(errors, "stderr")

        #We should add more testcases that are more relevant in the future...
