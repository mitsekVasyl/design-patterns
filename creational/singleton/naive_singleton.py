class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            print(cls._instances)
            print(cls._instances[cls])

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def do_staff(self):
        print(f"{self}")


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print("Is it the same instance?\n", id(s1) == id(s2))
