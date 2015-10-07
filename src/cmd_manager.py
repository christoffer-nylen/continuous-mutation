import subprocess

class CommandManager:
    def run(self, command, args=''):
        if(args == ''):
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            p = subprocess.Popen([command, args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out.decode('unicode_escape'), err.decode('unicode_escape')

if __name__ == "__main__":
    #Code to be run by the test
    import sys
    sys.stdout.write("stdout")
    sys.stderr.write("stderr")
