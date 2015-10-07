import subprocess

class CommandManager:
    def run(self, command, flags=''):
        if(flags == ''):
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            p = subprocess.Popen([command, flags], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out.decode('unicode_escape'), err.decode('unicode_escape')

class GccParser:
    def __init__(self):

    
cmdManager = CommandManager()

output, errors = cmdManager.run("ls")

print("Output: ")
print(output)

print("")

print("Errors: ")
print(errors)

output, errors = cmdManager.run("python3", "xml_mutation.py")

print("Output: ")
print(output)

print("")

print("Errors: ")
print(errors)

output, errors = cmdManager.run("cat", "finnsej.py")

print("Output: ")
print(output)

print("")

print("Errors: ")
print(errors)
