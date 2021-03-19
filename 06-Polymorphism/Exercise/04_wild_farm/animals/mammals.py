from animals.animal import Mammal
from food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10


    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.gain_weight(Mouse.WEIGHT_INCREASE, food)


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.gain_weight(Dog.WEIGHT_INCREASE, food)


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.gain_weight(Cat.WEIGHT_INCREASE, food)


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.gain_weight(Tiger.WEIGHT_INCREASE, food)
