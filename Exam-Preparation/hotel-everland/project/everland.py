from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(
            [r.total_expenses for r in self.rooms]
        )

        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        result = ''

        for room in self.rooms:
            if room.budget <= room.total_expenses:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
            else:
                room.budget -= room.total_expenses
                result += f"{room.family_name} paid {room.total_expenses:.2f}$ and have {room.budget:.2f}$ left.\n"

        return result[:-1]

    def status(self):
        result = ''

        total_population = sum([r.members_count for r in self.rooms])

        result += f"Total population: {total_population}\n"

        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. " \
                      f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"

            for index, child in enumerate(room.children, start=1):
                result += f"--- Child {index} monthly cost: {child.get_monthly_expense():.2f}$\n"

            total_appliances_cost = sum([a.get_monthly_expense() for a in room.appliances])

            result += f"--- Appliances monthly cost: {total_appliances_cost:.2f}$\n"

        return result[:-1]
