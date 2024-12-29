from food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, prise):
        super().__init__(name, prise, Salmon.GRAMS)
