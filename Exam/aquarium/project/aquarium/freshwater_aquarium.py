from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    initial_capacity = 50

    def __init__(self, name: str):
        super().__init__(name, self.initial_capacity)
