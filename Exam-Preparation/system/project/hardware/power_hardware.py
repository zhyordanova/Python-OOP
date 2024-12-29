from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    default_type = 'Power'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.default_type, int(capacity * 0.25), int(memory * 1.75))
