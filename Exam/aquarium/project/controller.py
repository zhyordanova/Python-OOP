from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def find_aquarium_by_name(self, name):
        try:
            aquarium = [a for a in self.aquariums if a.name == name][0]
            return aquarium
        except IndexError:
            return

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_type = ('FreshwaterAquarium', 'SaltwaterAquarium')

        if aquarium_type not in valid_type:
            return "Invalid aquarium type."

        if aquarium_type == valid_type[0]:
            new_aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == valid_type[1]:
            new_aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        valid_type = ('Ornament', 'Plant')

        if decoration_type not in valid_type:
            return "Invalid decoration type."

        if decoration_type == valid_type[0]:
            new_decoration = Ornament()
        elif decoration_type == valid_type[1]:
            new_decoration = Plant()

        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.find_aquarium_by_name(aquarium_name)

        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish_type = ('FreshwaterFish', 'SaltwaterFish')
        valid_aquarium_type = ('FreshwaterAquarium', 'SaltwaterAquarium')

        if fish_type not in valid_fish_type:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.find_aquarium_by_name(aquarium_name)

        if fish_type == valid_fish_type[0] and aquarium.__class__.__name__ == valid_aquarium_type[0]:
            new_fish = FreshwaterFish(fish_name, fish_species, price)
            return aquarium.add_fish(new_fish)
        elif fish_type == valid_fish_type[1] and aquarium.__class__.__name__ == valid_aquarium_type[1]:
            new_fish = SaltwaterFish(fish_name, fish_species, price)
            return aquarium.add_fish(new_fish)
        else:
            return f"Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)

        value = aquarium.total_value
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = '\n'.join([str(a) for a in self.aquariums])

        return result[:-1]
