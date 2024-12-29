from project.supply.supply import Supply


class WaterSupply(Supply):
    initial_needs_increase = 40

    def __init__(self):
        super().__init__(self.initial_needs_increase)