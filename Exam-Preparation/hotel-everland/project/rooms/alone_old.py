from project.rooms.room import Room


class AloneOld(Room):
    default_member_count = 1
    room_cost = 10
    
    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, self.default_member_count)
