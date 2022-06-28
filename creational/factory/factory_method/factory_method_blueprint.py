from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def do_staff(self):
        product = self.factory_method()

        return f"Created product of type: {type(product)}. Product operation: {product.operation()}"


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreateCreator1(Creator):

    def factory_method(self):
        return ConcreateProduct1()


class ConcreateCreator2(Creator):

    def factory_method(self):
        return ConcreateProduct2()


"""
Products
"""


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreateProduct1(Product):

    def operation(self) -> str:
        return "ConcreateProduct1 operation"


class ConcreateProduct2(Product):

    def operation(self) -> str:
        return "ConcreateProduct2 operation"


"""
Client code
"""


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.do_staff()}", end="")


if __name__ == '__main__':
    client_code(ConcreateCreator1())
    print('\n')
    client_code(ConcreateCreator2())
