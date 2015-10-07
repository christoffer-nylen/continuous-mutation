import subprocess

class CommandManager:
    def run(self, command, *args):
        list = [command]
        for arg in args:
            list.append(arg)
        p = subprocess.Popen(list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out.decode('unicode_escape'), err.decode('unicode_escape')
