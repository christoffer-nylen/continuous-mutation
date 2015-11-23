#! /usr/bin/env python3

import sys
import database.dbhandler
import command_manager.cmd_manager
import pyfilter

##
# @param command is a list of arguments, where command[0] is the program to execute
# @returns List of strings of matching errors

def run_with_error_support(command):
    """
    Runs a command and attempts to find appropriate error in database
    """
    _, error = command_manager.cmd_manager.CommandManager.run(None, command[0], *command[1:])
    if error.rstrip() == "":
        return []

    parse_filter = pyfilter.Filter();
    error = parse_filter.parse(error)
    
    try:
        return [(node,error) for node in database.dbhandler.find(error)]
    except:
        print("{}: ".format(sys.argv[0]), *sys.exc_info()[:-1])
        print("{}: Has the database been initialized?".format(sys.argv[0]))
        return []

if __name__ == "__main__":
    command = sys.argv[1:]
    possible_solutions = run_with_error_support(command)
    if possible_solutions == []:
        print("\n{}: No matching errors found in database".format(sys.argv[0]))
        sys.exit(0)

    if len(possible_solutions) == 1:
        print("\n{}: Possibly caused by this missing tag:".format(sys.argv[0]))
    else:
        print("\n{}: Possibly caused by any of these missing tags:".format(sys.argv[0]))

    for (node, error) in possible_solutions:
        print("Hit accuracy: " , (len(error) / len(node[0])) * 100, "%" )
        print(*node[1:])
