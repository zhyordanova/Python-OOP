from project.software.software import Software


class LightSoftware(Software):
    default_type = 'Light'

    def __init__(self, name, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.default_type, int(capacity_consumption * 1.5), int(memory_consumption * 0.5))
