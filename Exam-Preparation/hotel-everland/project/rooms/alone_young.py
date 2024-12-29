from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    default_member_count = 1
    room_cost = 10
    appliance_types = (TV,)

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.default_member_count)
        self.calculate_expenses(self.appliances)
