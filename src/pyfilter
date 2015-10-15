#! /usr/bin/env python3

import sys
import argparse
import re
import fileinput


class Filter:
    def __init__(self, args):
        self.remove_path = args.remove_path
        self.remove_namespaces = args.remove_namespaces
        self.only_error = args.only_error

        self.error_type = "Compilation Error"
        self.signal_eof = False

    def parse(self, source):
        """
        Parses given source

        Args:
            source:     Given source, e.g. sys.stdin

        Returns:
            A string containing the parse output

        """
        return_value = "".join(self.parse_line(line) for line in source)
        return "\n".join([self.error_type, return_value])

    def parse_line(self, line):
        """
        Parse line of file

        Args:
            line:       String to parse

        Returns:
            A string containing the parse output
        """
        if self.signal_eof:
            return ""

        match = re.search("^([\w\s]+from) ([^:]+):(\d+)(:|,)$", line)
        if match:
            return self.parse_line_from(match)

        match = re.search("^([^:]+):(?:((?:\d+:)?\d+):)?(?:(error|warning|note):)?(.+)$", line)
        if match:
            return self.parse_line_err(match)

        return line

    def fix_filename(self):
        """
        Remove paths from filenames on the current line being parsed

        Example:
            /var/log/auth.log becomes .../auth.log
        """
        if not self.remove_path:
            return
        self.filename = re.sub(".+\/", ".../", self.filename)

    def fix_namespaces(self):
        """
        Removes namespaces on the current line being parsed

        Example:
            IO::Hello::hi() becomes hi()
        """
        if not self.remove_namespaces:
            return
        self.message = re.sub("[A-Za-z0-9_]+::", "", self.message)

    def fix_nonerrors(self):
        """
        Remove line number and filename from current line being parsed

        Example:
            /home/chrny/my_builds/csu_a/test_suite/driver.cpp:46:
                undefined reference to `CSU_A::Run()'

            becomes

            undefined reference to `CSU_A::Run()'
        """
        if not self.only_error:
            return
        self.line = None
        self.filename = None

    def parse_line_from(self, match):
        """
        Function for parsing lines containing "from", like "included from file".
        This function should only be called from parse_line
        """
        self.line = match.group(3)
        self.filename = match.group(2)
        self.message = match.group(1)
        self.eoli = match.group(4)

        self.fix_filename()
        self.fix_namespaces()
        self.fix_nonerrors()

        if self.filename is None or self.line is None:
            return ""
        else:
            return "{} {}:{}{}\n".format(self.message, self.filename, self.line, self.eoli)

    def parse_line_err(self, match):
        """
        Function for parsing generic lines. Should only be called from
        parse_line
        """
        self.line = match.group(2)
        self.filename = match.group(1)
        self.message = match.group(4)
        self.keyword = match.group(3)

        self.fix_filename()
        self.fix_namespaces()
        self.fix_nonerrors()

        if self.message.strip() == "ld returned 1 exit status":
            self.error_type = "Linking Error"
            self.signal_eof = True
            return ""

        return_value = ""
        if self.filename is not None:
            return_value += "{}:".format(self.filename)
        if self.line is not None:
            return_value += "{}: ".format(self.line)
        if self.keyword is not None:
            return_value += "{}: ".format(self.keyword)
        if self.message is not None:
            return_value += self.message

        if return_value != "":
            return_value += "\n"
        return return_value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter g++ output")
    parser.add_argument("-E", "--no-only-error", dest="only_error",
                        default=True, action="store_false", help="Show more info than just error")
    parser.add_argument("-n", "--no-namespaces", dest="remove_namespaces",
                        default=False, action="store_true", help="Remove namespaces")
    parser.add_argument("-p", "--no-path", dest="remove_path",
                        default=False, action="store_true", help="Remove filepath")
    args = parser.parse_args()

    print(Filter(args).parse(sys.stdin), end="")
