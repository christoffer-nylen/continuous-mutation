#! /usr/bin/env python3

import sys

import continuous_mutation.client as client
import continuous_mutation.run_mutator as run_mutator

def unknown_argument():
    print("Please use either 'client' or 'run_mutator' as first argument")


def client_arguments(args):
    def usage():
        print("Usage: client database_path commands",
              "Example: client sqlite.db make Makefiles",
              sep="\n\n")

    try:
        program_name = sys.argv[1]
        database_name = sys.argv[2]
        command = sys.argv[3:]
        if len(command) == 0:
            raise
        return program_name, database_name, command
    except:
        usage()
        sys.exit(1)


def run_mutator_arguments(args):
    def usage():
        print("Usage: run_mutator xml_file database_path",
              "Example: run_mutator test_constellations.xml sqlite.db",
              sep="\n\n")

    try:
        file_name = args[2]
        database_name = args[3]
        return file_name, database_name
    except:
        usage()
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        unknown_argument()
    elif sys.argv[1] == "client":
        client.main(*client_arguments(sys.argv))
    elif sys.argv[1] == "run_mutator":
        run_mutator.main(*run_mutator_arguments(sys.argv))
    else:
        unknown_argument()
