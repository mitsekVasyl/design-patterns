from enum import Enum
import time


PizzaProgres = Enum("PizzaProgres", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme")
PizzaTopping = Enum("PizzaTopping", "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano")


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f"Preparing the {self.dough.name} dough of your {self}...")
        time.sleep(2)
        print(f"Done with the {self.dough.name} dough")


class MargaritaBuilder:

    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgres.queued
        self.baking_time = 5  # in seconds

    def prepare_dough(self):
        self.progress = PizzaProgres.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("Adding the tomato sauce...")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(2)
        print("Done with the tomato sauce.")

    def add_topping(self):
        topping_desc = "double mozzarella, oregano"
        topping_items = (PizzaTopping.double_mozzarella, PizzaTopping.oregano)
        print(f"Adding the topping ({topping_desc}) to your margarita")
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(2)
        print("Done with toppings")

    def bake(self):
        self.progress = PizzaProgres.baking
        print("Baking margarita")
        time.sleep(3)
        self.progress = PizzaProgres.ready
        print("Margarita is ready")


class CreamyBaconBuilder:

    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgres.queued
        self.baking_time = 5  # in seconds

    def prepare_dough(self):
        self.progress = PizzaProgres.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print("Adding the creme sauce...")
        self.pizza.sauce = PizzaSauce.creme
        time.sleep(2)
        print("Done with the creme sauce.")

    def add_topping(self):
        topping_desc = "mozzarella, bacon, ham, mushrooms, red_onion, oregano"
        topping_items = (PizzaTopping.mozzarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregano)
        print(f"Adding the topping ({topping_desc}) to your creamy bacon")
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(2)
        print("Done with toppings")

    def bake(self):
        self.progress = PizzaProgres.baking
        print("Baking Creamy bacon")
        time.sleep(3)
        self.progress = PizzaProgres.ready
        print("Creamy bacon is ready")


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)

        for step in steps:
            step()

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        input_msg = "Choose pizza: [m]argarita [c]reamy bacon "
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = "We don't have such pizza"
        print(error_msg)
        return False, None

    return True, builder


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)

    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f"Enjoy your {pizza}!")


if __name__ == "__main__":
    main()
