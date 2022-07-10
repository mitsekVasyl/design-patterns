from abc import ABC, abstractmethod


class Context:

    def __init__(self, state):
        self._state = state
        self.set_state(state)

    def set_state(self, state):
        self._state = state
        self._state._context = self

    def do_staff(self):
        """Delegates work to a concrete state"""
        print(f"I'm a context. Delegating work to {self._state}")
        self._state.do_staff()

    def do_another_staff(self):
        """Delegates work to a concrete state"""
        print(f"I'm a context. Delegating another work to {self._state}")
        self._state.do_another_staff()


class State(ABC):

    def __init__(self):
        self._context = None

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def do_staff(self):
        pass

    @abstractmethod
    def do_another_staff(self):
        pass


class ConcreteStateA(State):

    def do_staff(self):
        print(f"I'm a ConcreteStateA. Doing staff and changing state to ConcreteStateB")
        self._context.set_state(ConcreteStateB())

    def do_another_staff(self):
        print(f"I'm a ConcreteStateA. Doing another staff")

    def __str__(self):
        return "ConcreteStateA"


class ConcreteStateB(State):

    def do_staff(self):
        print(f"I'm a ConcreteStateB. Doing staff")

    def do_another_staff(self):
        print(f"I'm a ConcreteStateB. Doing another staff and changing state to ConcreteStateA")
        self._context.set_state(ConcreteStateA())

    def __str__(self):
        return "ConcreteStateB"


if __name__ == "__main__":
    state_a = ConcreteStateA()

    context_1 = Context(state_a)
    context_1.do_staff()
    context_1.do_another_staff()
    context_1.do_another_staff()
