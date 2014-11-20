import subprocess
import sublime, sublime_plugin

# Extends TextCommand so that run() receives a View to modify.
class DaniCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pass

def run_shell_cmd(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')