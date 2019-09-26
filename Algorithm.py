import importlib
import sys

sys.path.insert(0, './algorithms')

class Algorithm:
    def __init__(self, ID):
        self.ID = ID
        self.script = importlib.import_module(ID)

    def run(self):
        self.script.run()
