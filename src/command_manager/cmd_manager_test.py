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

    def testPythonScript(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("python3", "test_stdout_stderr.py")
        self.assertEqual(output, "stdout")
        self.assertEqual(errors, "stderr")

    def testArguments(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("cat", "-n", "test_stdout_stderr.py")
        self.assertTrue(len(output) > 0)
        self.assertEqual(errors, "")

    def testCompileCplusplus(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("g++", "test_stdout_stderr.cpp")
        self.assertEqual(output, "")
        self.assertEqual(errors, "")

    def testRunCplusplus(self):
        cmdManager = CommandManager()
        output, errors = cmdManager.run("./a.out")
        self.assertEqual(output, "stdout")
        self.assertEqual(errors, "stderr")

        # We should add more testcases that are more relevant in the future...

TestCmdManager().testCompileCplusplus();
