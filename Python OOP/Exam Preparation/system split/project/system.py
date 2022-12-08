from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_exists = ''

        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware_exists = hardware

        if hardware_exists == '':
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware_exists.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_exists = ''

        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware_exists = hardware

        if hardware_exists == '':
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware_exists.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware_exists = ''
        software_exists = ''

        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware_exists = hardware

        for software in System._software:
            if software.name == software_name:
                software_exists = software

        if hardware_exists == '' and software_exists == '':
            return "Some of the components do not exist"

        hardware_exists.uninstall(software_exists)
        System._software.remove(software_exists)

    @staticmethod
    def analyze():
        result = "System Analysis" +\
                 '\n' + f'Hardware Components: {len(System._hardware)}' \
                 + '\n' + f'Software Components: {len(System._software)}' \
                 + '\n' + f'Total Operational Memory: {sum(s.memory_consumption for s in System._software)} / {sum(h.memory for h in System._hardware)}' +\
                 '\n' + f'Total Capacity Taken: {sum(s.capacity_consumption for s in System._software)} / {sum(h.capacity for h in System._hardware)}'
        return result

    @staticmethod
    def system_split():

        result = ''
        for hardware in System._hardware:
            result += f'Hardware Component - {hardware.name}' + '\n'
            result += f"Express Software Components: {len([c.name for c in hardware.software_components if c.software_type =='Express'])}" + '\n'
            result += f"Light Software Components: {len([c.name for c in hardware.software_components if c.software_type == 'Light'])}" + '\n'
            result += f"Memory Usage: {sum(s.memory_consumption for s in hardware.software_components)} / {hardware.memory}" + '\n'
            result += f"Capacity Usage: {sum(s.capacity_consumption for s in hardware.software_components)} / {hardware.capacity}" + '\n'
            result += f"Type: {hardware.hardware_type}" + '\n'
            software_components_separated_by_coma = ', '.join(c.name for c in hardware.software_components)
            result += f"Software Components: {software_components_separated_by_coma if hardware.software_components else None }" + '\n'

        return result.strip()





