from abc import ABC, abstractmethod


class IComputerFactory(ABC):
    """
    Abstract factory for creating different types of computers.
    """
    @abstractmethod
    def create_notebook(self):
        pass

    @abstractmethod
    def create_tablet(self):
        pass


class AppleFactory(IComputerFactory):
    """
    Factory to produce Apple computers.
    """
    def create_notebook(self):
        print("Building Apple notebook...")
        return AppleMacBook()

    def create_tablet(self):
        print("Building Apple tablet...")
        return AppleIpad()


class MicrosoftFactory(IComputerFactory):
    """
    Factory to produce Microsoft computers.
    """

    def create_notebook(self):
        print("Building Microsoft notebook...")
        return MicrosoftChromeBook()

    def create_tablet(self):
        print("Building Microsoft tablet...")
        return MicrosoftSurface()


class AbstractNotebook(ABC):

    @abstractmethod
    def supply_notebook(self):
        pass


class AppleMacBook(AbstractNotebook):

    def supply_notebook(self):
        return "I'm MacBook!"


class MicrosoftChromeBook(AbstractNotebook):

    def supply_notebook(self):
        return "I'm Microsoft ChromeBook!"


class AbstractTablet(ABC):

    @abstractmethod
    def supply_tablet(self):
        pass


class AppleIpad(AbstractTablet):

    def supply_tablet(self):
        return "I'm Apple Ipad!"


class MicrosoftSurface(AbstractTablet):

    def supply_tablet(self):
        return "I'm Microsoft Surface tablet!"


def client_code(factory: IComputerFactory) -> None:
    notebook = factory.create_notebook()
    print(f"{notebook.supply_notebook()}")

    tablet = factory.create_tablet()
    print(f"{tablet.supply_tablet()}")


if __name__ == "__main__":

    print("Client: Testing Aplle factory:")
    client_code(AppleFactory())

    print("\n")

    print("Client: Testing Microsoft factory:")
    client_code(MicrosoftFactory())
