from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    default_type = 'Heavy'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.default_type, capacity * 2, int(memory * 0.75))
