class Target:
    """Domain specific interface."""

    def request(self):
        return "Target: The default target's behavior."


class Adaptee:
    """Incompatible interface."""

    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):

    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target):
    print(target.request())


if __name__ == "__main__":
    target = Target()
    client_code(target)

    adapter = Adapter(Adaptee())
    client_code(adapter)
