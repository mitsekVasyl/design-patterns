from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):

    def __init__(self, receiver, *args):
        self._params = args
        self._receiver = receiver

    def execute(self):
        print("I'm concrete command. Passing request with params to the receiver.")
        self._receiver.operation(*self._params)


class Invoker:

    def __init__(self, command):
        self._command = command

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        print("I'm invoker. Delegating work to concrete command.")
        self._command.execute()


class Receiver:

    def operation(self, param1, param2):
        print("Doing some operation with params:", param1, param2)


if __name__ == "__main__":
    rec = Receiver()
    concrete_command = ConcreteCommand(rec, "param1", "param2")
    invoker = Invoker(concrete_command)

    invoker.execute_command()


