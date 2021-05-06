from project.supply.supply import Supply


class FoodSupply(Supply):
    initial_needs_increase = 20

    def __init__(self):
        super().__init__(self.initial_needs_increase)
