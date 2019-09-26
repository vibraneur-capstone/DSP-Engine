import importlib

class Algorithm:
    def __init__(self, filename, ID):
        self.filename = ".algorithms." + filename + ".py"
        self.ID = importlib.import_module(filename)

    def run():
        self.ID.run()
