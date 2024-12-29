from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = [f for f in self.supplies if f.__class__.__name__ == 'FoodSupply']
        if len(foods) == 0:
            raise IndexError("There are no food supplies left!")
        return foods

    @property
    def water(self):
        water = [w for w in self.supplies if w.__class__.__name__ == 'WaterSupply']
        if len(water) == 0:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers = [p for p in self.medicine if p.__class__.__name__ == "Painkiller"]
        if len(painkillers) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [s for s in self.supplies if s.__class__.__name__ == "Salve"]
        if len(salves) == 0:
            raise IndexError("There are no salves left!")
        return salves


    def add_survivor(self, survivor: Survivor):

        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")

        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type):
        if survivor.needs_healing:
            if medicine_type == "Painkiller":
                med = self.painkillers[-1]

            elif medicine_type == "Salve":
                med = self.salves[-1]

            self.medicine.remove(med)
            med.apply(survivor)

            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                supply = self.food[-1]

            elif sustenance_type == "WaterSupply":
                supply = self.water[-1]

            self.supplies.remove(supply)
            supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")


