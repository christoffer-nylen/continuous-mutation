import unittest
import os
from continuous_mutation.command_manager.cmd_manager import CommandManager
"""
testing cmd_manager.py in command_manager/
"""

path = os.path.dirname(__file__)
if path == "":
    path = "."

class TestCmdManager(unittest.TestCase):

    def testOutput(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("printf", "Test")
        self.assertEqual(errors, "")
        self.assertEqual(output, "Test")

    def testError(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("printf")
        self.assertEqual(errors, "printf: missing operand\nTry 'printf --help' for more information.\n")
        self.assertEqual(output, "")
        self.assertTrue(len(errors) > 0)

    def testPythonScript(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("python3", path + "/test_stdout_stderr.py")
        self.assertEqual(output, "stdout")
        self.assertEqual(errors, "stderr")

    def testArguments(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("cat", "-n", path + "/test_stdout_stderr.py")
        self.assertTrue(len(output) > 0)
        self.assertEqual(errors, "")

    """
    def testCompileCplusplus(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("g++", path + "/test_stdout_stderr.cpp")
        self.assertEqual(output, "")
        self.assertEqual(errors, "")

    def testRunCplusplus(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("./a.out")
        self.assertEqual(output, "stdout")
        self.assertEqual(errors, "stderr")
    """


unittest.main()
