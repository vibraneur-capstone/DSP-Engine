class DSPEngine:

    def __init__(self):
        self.algorithms = []

    def run(self, data):
        for a in self.algorithms:
            a.call(data)

    def add(self, algorithm):
        self.algorithms.append(algorithm)

    def remove(self, algorithm):
        self.algorithms.remove(algorithm)
