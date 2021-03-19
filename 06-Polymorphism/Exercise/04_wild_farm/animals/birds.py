from animals.animal import Bird
from food import Meat


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.gain_weight(Owl.WEIGHT_INCREASE, food)



class Hen(Bird):

    WEIGHT_INCREASE = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.gain_weight(Hen.WEIGHT_INCREASE, food)

