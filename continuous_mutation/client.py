#! /usr/bin/env python3

import sys

import continuous_mutation.command_manager.cmd_manager as cmd_mgr
import continuous_mutation.python_filter.pyfilter as pyfilter

from continuous_mutation.database.dbhandler import DatabaseHandler

"""
@param
    command is a list of arguments, where command[0] is the program to execute.
@returns
    List of strings of matching errors
"""
def run_with_error_support(program_name, database_name, command):
    """
    Runs a command and attempts to find appropriate error in database

    Example: run_with_error_support(["make", "Makefiles"])
    """

    dbhandler = DatabaseHandler(database_name)
    _, error = cmd_mgr.CommandManager.run(None, command[0], *command[1:])


    if error.rstrip() == "":
        return []

    parse_filter = pyfilter.Filter()
    error = parse_filter.parse(error)

    try:
        return [(node, error) for node in dbhandler.find(error)]
    except:
        print("{}: ".format(program_name), *sys.exc_info()[:-1])
        print("{}: Has the database been initialized?".format(program_name))
        return []

def main(program_name, database_name, commands):
    possible_solutions = run_with_error_support(program_name, database_name,
            commands)
    if possible_solutions == []:
        print("\n{}: No matching errors found in database".format(program_name))
        sys.exit(0)

    if len(possible_solutions) == 1:
        print("\n{}: Possibly caused by this missing tag:".format(program_name))
    else:
        print("\n{}: ".format(program_name),
              "Possibly caused by any of these missing tags:")

    for (node, error) in possible_solutions:
        try:
            accuracy = (len(error) / len(node[0])) * 100
        except ZeroDivisionError:
            accuracy = 0
        print("Hit accuracy: {}%".format(accuracy), *node[1:])

if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1], sys.argv[2:])
