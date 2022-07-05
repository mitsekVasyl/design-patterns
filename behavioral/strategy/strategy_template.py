from abc import ABC, abstractmethod


class IStrategy(ABC):

    @abstractmethod
    def execute(self):
        pass


class ConcreteStrategy1(IStrategy):

    def execute(self):
        print("Executing concrete strategy #1")


class ConcreteStrategy2(IStrategy):

    def execute(self):
        print("Executing concrete strategy #2")


class Context:

    def __init__(self, strategy: IStrategy):
        self._strategy = strategy

    def do_staff(self):
        self._strategy.execute()


if __name__ == "__main__":
    context = Context(ConcreteStrategy1())
    context.do_staff()

    context = Context(ConcreteStrategy2())
    context.do_staff()
