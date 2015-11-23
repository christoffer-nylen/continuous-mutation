#! /usr/bin/env python3

import sys
import re
import os

class Filter:
    def __init__(self, regex_file_path=""):

        # Default regex_file:
        if regex_file_path == "":
            filedir = os.path.dirname(__file__)
            if filedir == "":
                filedir = "."
            regex_file_path = "{}/filter_list.txt".format(filedir)

        # Compile all lines as regexes
        self.regex_list = []
        with open(regex_file_path, "r") as f:
            for line in f:
                self.regex_list.append(re.compile(line.strip()))


    ##
    # @param source Given source, e.g. sys.stdin
    # @returns A string containing the parse output
    def parse(self, source):
        """
        Parses given source
        """
        return "".join(self.parse_line(line) for line in source)


    ##
    # @param line String to parse
    # @returns A string containing the parse output, which is empty when there is no match
    def parse_line(self, line):
        """
        Parse line of file
        """
        for regex in self.regex_list:
            match = regex.search(line)
            if match:
                return "{}\n".format(match.group(0))
        return ""


if __name__ == "__main__":
    print(Filter().parse(sys.stdin), end="")
