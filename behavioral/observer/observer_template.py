from abc import ABC, abstractmethod


class ISubscriber(ABC):

    @abstractmethod
    def update(self, context):
        pass


class Subscriber1(ISubscriber):

    def update(self, context):
        print(f"Subscriber1: Event update with context: {context}!")

    def __str__(self):
        return "Subscriber1"


class Subscriber2(ISubscriber):

    def update(self, context):
        print(f"Subscriber2: Event update with context: {context}!")

    def __str__(self):
        return "Subscriber2"


class Publisher:
    def __init__(self):
        self._subscribers = []
        self._context = None

    def subscribe(self, subscriber):
        print(f"subscribing {subscriber}")
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        print(f"unsubscribing {subscriber}")
        del self._subscribers[self._subscribers.index(subscriber)]

    def notify_subscriber(self, context):
        for subscriber in self._subscribers:
            subscriber.update(context)

    def business_logic(self, context):
        self._context = context
        self.notify_subscriber(self._context)


# client code
if __name__ == "__main__":
    subscriber1 = Subscriber1()
    subscriber2 = Subscriber2()

    publisher = Publisher()

    publisher.subscribe(subscriber1)
    publisher.business_logic(context="Hello world")

    publisher.subscribe(subscriber2)
    publisher.business_logic(context="Hello!")

    publisher.unsubscribe(subscriber1)
    publisher.business_logic(context="Hello! Hello!")

