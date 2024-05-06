class Saga():
    def __init__(self, actions):
        self.actions = actions

    def execute(self):
        for action, _ in self.actions:
            action()

    def compensate(self):
        for _, compensation in reversed(self.actions):
            compensation()
