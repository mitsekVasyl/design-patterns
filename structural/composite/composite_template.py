from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def do_staff(self):
        pass


class Composite(Component):

    def __init__(self):
        self._components = []

    # implementing methods to work with child here because I don't want to break interface segregation principle
    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        component_idx = self._components.index(component)
        del self._components[component_idx]

    def get_children(self):
        return self._components

    def do_staff(self):
        print("I'm a composite! Getting children and doing something")
        for component in self.get_children():
            component.do_staff()


class Leaf(Component):

    def do_staff(self):
        print("I'm a leaf. Doing my best!")


if __name__ == "__main__":

    leaf_a = Leaf()
    leaf_b = Leaf()
    leaf_c = Leaf()

    print("\nPrinting composite A with it leaves")
    composite_a = Composite()
    composite_a.add_component(leaf_a)
    composite_a.add_component(leaf_b)
    composite_a.do_staff()

    print("\nExecuting composite A with composite B and theirs leaves")
    composite_b = Composite()
    composite_b.add_component(leaf_c)
    composite_a.add_component(composite_b)
    composite_a.do_staff()


