class BaseAgent:
    def __init__(self, name):
        self.name = name

    def execute(self, query):
        raise NotImplementedError("Subclasses must implement the execute method")


