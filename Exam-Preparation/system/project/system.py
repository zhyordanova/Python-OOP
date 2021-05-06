from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heave_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heave_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)

            hardware.install(software)
            System._software.append(software)

        except IndexError:
            return "Hardware does not exist"

        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)

            hardware.install(software)
            System._software.append(software)

        except IndexError:
            return "Hardware does not exist"

        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]

            hardware.uninstall(software)
            System._software.remove(software)

        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_used_memory = sum([h.used_memory for h in System._hardware])
        total_memory = sum([h.memory for h in System._hardware])
        total_used_capacity = sum([h.used_capacity for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])

        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {total_used_capacity} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ''

        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"

            express_software = len([s for s in hardware.software_components if s.type == 'Express'])
            light_software = len([s for s in hardware.software_components if s.type == 'Light'])
            total_memory_usage = sum([s.memory_consumption for s in hardware.software_components])
            total_capacity_usage = sum([s.capacity_consumption for s in hardware.software_components])
            software_components = ', '.join([s.name for s in hardware.software_components]) \
                if hardware.software_components else 'None'

            result += f"Express Software Components: {express_software}\n" \
                      f"Light Software Components: {light_software}\n" \
                      f"Memory Usage: {total_memory_usage} / {hardware.memory}\n" \
                      f"Capacity Usage: {total_capacity_usage} / {hardware.capacity}\n" \
                      f"Type: {hardware.type}\n" \
                      f"Software Components: {software_components}"

        return result
