from project.medicine.medicine import Medicine


class Salve(Medicine):
    initial_health_increase = 50

    def __init__(self):
        super().__init__(self.initial_health_increase)
