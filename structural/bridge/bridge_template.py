from abc import ABC, abstractmethod


class Implementation(ABC):

    @abstractmethod
    def method_1(self):
        pass

    @abstractmethod
    def method_2(self):
        pass

    @abstractmethod
    def method_3(self):
        pass


class Abstraction(ABC):

    def __init__(self, implementation: Implementation):
        self._implementation = implementation

    @abstractmethod
    def feature_1(self):
        pass

    @abstractmethod
    def feature_2(self):
        pass


class ConcreteAbstraction(Abstraction):

    def feature_1(self):
        print("\nDoing feature 1 of ConcreteAbstraction")
        self._implementation.method_1()
        self._implementation.method_2()

    def feature_2(self):
        print("\nDoing feature 2 of ConcreteAbstraction")
        self._implementation.method_3()


class ConcreteImplementationA(Implementation):

    def method_1(self):
        print("Concrete implementation A: method_1")

    def method_2(self):
        print("Concrete implementation A: method_2")

    def method_3(self):
        print("Concrete implementation A: method_3")


class ConcreteImplementationB(Implementation):

    def method_1(self):
        print("Concrete implementation B: method_1")

    def method_2(self):
        print("Concrete implementation B: method_2")

    def method_3(self):
        print("Concrete implementation B: method_3")


if __name__ == "__main__":
    concrete_implementation_a = ConcreteImplementationA()
    abstraction = ConcreteAbstraction(concrete_implementation_a)
    abstraction.feature_1()
    abstraction.feature_2()
    print()
    concrete_implementation_b = ConcreteImplementationB()
    abstraction = ConcreteAbstraction(concrete_implementation_b)
    abstraction.feature_1()
    abstraction.feature_2()
