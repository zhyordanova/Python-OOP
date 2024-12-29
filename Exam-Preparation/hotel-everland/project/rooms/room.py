class Room:
    room_cost = 0
    appliance_types = ()
    
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = self.get_appliances(*self.appliance_types)
        self.expenses = 0

    @staticmethod
    def __validate_expenses(value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        self.__validate_expenses(value)
        self.__expenses = value

    @property
    def total_expenses(self):
        return self.expenses + self.room_cost

    def calculate_expenses(self, *args):
        result = 0

        for items in args:
            result += sum(
                [x.get_monthly_expense() for x in items]
            )

        self.expenses = result

    def get_appliances(self, *appliance_types):
        appliances = []

        for _ in range(self.members_count):
            for appliance_type in appliance_types:
                appliances.append(appliance_type())

        return appliances


