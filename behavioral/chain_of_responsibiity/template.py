from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def set_next_handler(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class BaseHandler(Handler):

    def __init__(self):
        self._next_handler = None

    def set_next_handler(self, handler: Handler):
        self._next_handler = handler

    def handle(self, request):
        if request and "a" in request:
            print("I'm a base handler! Handling request")
            print("Request:", request)

        elif self._next_handler:
            self._next_handler.handle(request)  # pass request to the next handler

        else:
            print("I'm a base handler! Can't handle and the next handle doesn't exist")


class ConcreteHandler(BaseHandler):

    def handle(self, request):
        if request and "b" in request:
            print("I'm concrete handler! Handling in other way")
            print("Request:", request)

        elif self._next_handler:
            self._next_handler.handle(request)

        else:
            print("I'm concrete handler! Can't handle and the next handle doesn't exist")


if __name__ == "__main__":
    base_handler = BaseHandler()
    concrete_handler = ConcreteHandler()

    print("\nHandling an empty request with base handler only")
    base_handler.handle(request=dict())

    print("\nHandling valid request for the base handler")
    base_handler.handle(request=dict(a="Valid request for base handler"))

    base_handler.set_next_handler(concrete_handler)
    print("\nHandling an empty request with base + concrete handlers")
    base_handler.handle(request=dict())

    print("\nHandling valid request for the concrete handler")
    base_handler.handle(request=dict(b="Valid request for concrete handler"))
