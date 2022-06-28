from abc import ABC, abstractmethod


class Creator(ABC):
    """Interface to concreate creator."""

    @abstractmethod
    def factory_method(self):
        pass

    def build_computer(self):
        computer = self.factory_method()
        return computer


class AppleCreator(Creator):
    """Class to create Apple computers."""

    def factory_method(self):
        return AppleComputer()


class MicrosoftCreator(Creator):
    """Class to create Microsoft computers."""

    def factory_method(self):
        return MicrosoftComputer()


class Product(ABC):
    """Interface to concreate products."""
    @abstractmethod
    def supply_computer(self):
        pass


class AppleComputer(Product):

    def __init__(self):
        print("Building Apple computer")
        self.cpu = 'Intel Core i7'
        self.ram = "16Gb"
        self.ssd = "512Gb"

    def supply_computer(self):
        return f"Apple MacMini: {self.cpu}/{self.ram}/{self.ssd}"


class MicrosoftComputer(Product):

    def __init__(self):
        print("Building Microsoft computer")
        self.cpu = 'Intel Core i5'
        self.ram = "32Gb"
        self.ssd = "256Gb"

    def supply_computer(self):
        return f"Microsoft Surface: {self.cpu}/{self.ram}/{self.ssd}"


def client_code(creator: Creator) -> None:
    print(f"Supplied computer: "
          f"{creator.build_computer().supply_computer()}", end="")


if __name__ == '__main__':
    client_code(AppleCreator())
    print('\n')
    client_code(MicrosoftCreator())
    print('\n')
