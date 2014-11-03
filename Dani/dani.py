# import sys
# sys.path.append(["/opt/sublime_text/sublime.py", "/opt/sublime_text/sublime_plugin.py"])


import sublime, sublime_plugin

# Extends TextCommand so that run() receives a View to modify.
class DaniCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Walk through each region in the selection
        for region in self.view.sel():
            print(dir(region))
            # Only interested in empty regions, otherwise they may span multiple
            # lines, which doesn't make sense for this command.
            if region.empty():
                print(region)
            #     # Expand the region to the full line i4t resides on, excluding the newline
            #     line = self.view.line(region)
            #     # Extract the string for the line, and add a newline
            #     lineContents = self.view.substr(line) + '\n'

            #     # Add the text at the beginning of the line
            #     self.view.insert(edit, 0, lineContents)