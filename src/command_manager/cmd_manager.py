import subprocess
import sys
import select
import os
"""
Class for running terminal commands and receive stdout and stderr
"""

class CommandManager:
    ##
    # @param command Terminal command as a string, eg. "ls"
    # @param *args optional parameters (like flags or filenames) for the command
    # @returns Two strings, one representing stdout and the other is stderr
    def run(self, command, *args):
        """
        Function that runs a terminal command and handles the stdout and stderr
        from it
        """
        out = []
        err = []
        list = [command]
        for arg in args:
            list.append(arg)

        with subprocess.Popen(list, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
            readable = {
                p.stdout.fileno(): sys.stdout.buffer,
                p.stderr.fileno(): sys.stderr.buffer
            }

            while readable:
                for fd in select.select(readable, [], [])[0]:
                    data = os.read(fd, 1024)
                    if not data:
                        del readable[fd]
                    else:
                        if fd == p.stdout.fileno():
                            sys.stdout.write(data.decode('unicode_escape'))
                            out.append(data.decode('unicode_escape'))
                        if fd == p.stderr.fileno():
                            sys.stderr.write(data.decode('unicode_escape'))
                            err.append(data.decode('unicode_escape'))

        p.stdout.close()
        p.stderr.close()
        return ''.join(out), ''.join(err)
