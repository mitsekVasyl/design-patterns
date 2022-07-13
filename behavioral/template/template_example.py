from abc import ABC, abstractmethod


class Template(ABC):

    def template_method(self):
        print("\nExecuting algorithm")
        self.step1()
        self.step2()
        self.step3()
        self.step4()

    @abstractmethod
    def step1(self):
        pass

    def step2(self):
        print("Base implementation of step2")

    def step3(self):
        print("Base implementation of step3")

    def step4(self):
        print("Base implementation of step4")


class Algorithm1(Template):

    def step1(self):
        print("Algorithm1: implementation of abstract step1")

    def step2(self):
        print("Algorithm1: overriding implementation of step2")


class Algorithm2(Template):

    def step1(self):
        print("Algorithm2: implementation of abstract step1")

    def step4(self):
        print("Algorithm2: overriding implementation of step4")


if __name__ == "__main__":
    algorithm1 = Algorithm1()
    algorithm2 = Algorithm2()

    algorithm1.template_method()
    algorithm2.template_method()
