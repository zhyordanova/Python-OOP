from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    initial_health_increase = 20

    def __init__(self):
        super().__init__(self.initial_health_increase)
