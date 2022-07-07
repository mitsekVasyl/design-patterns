from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def do_stuff(self):
        pass


class ConcreteComponent1(Component):

    def do_stuff(self):
        print("ConcreteComponent1: doing something")

    def __str__(self):
        return "ConcreteComponent1"


class Decorator(Component):

    def __init__(self, component):
        self._component = component

    def do_stuff(self):
        pass


class ConcreteDecorator1(Decorator):

    def do_stuff(self):
        print(f"ConcreteDecorator1: Decorating component: {self._component}")
        self._component.do_stuff()

    def __str__(self):
        return "ConcreteDecorator1"


class ConcreteDecorator2(Decorator):

    def do_stuff(self):
        print(f"ConcreteDecorator2: Decorating component: {self._component}")
        self._component.do_stuff()

    def __str__(self):
        return "ConcreteDecorator2"


if __name__ == "__main__":
    print("\nwithout decorator")
    concrete_component = ConcreteComponent1()
    concrete_component.do_stuff()
    print("\none decorator")
    decorated_component1 = ConcreteDecorator1(concrete_component)
    decorated_component1.do_stuff()
    print("\ntwo decorators")
    decorated_component2 = ConcreteDecorator2(decorated_component1)
    decorated_component2.do_stuff()
