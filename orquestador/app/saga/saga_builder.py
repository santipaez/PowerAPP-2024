from collections.abc import Callable
from .saga import Saga

class SagaBuilder :
    def __init__(self):
        self.actions = []

    @staticmethod
    def create() -> 'SagaBuilder':
        return SagaBuilder()

    def action(self, action: Callable[[], None], compensation: Callable[[], None]) -> 'SagaBuilder':
        self.actions.append((action, compensation))
        return self

    def build(self) -> 'Saga':
        return Saga(self.actions)
