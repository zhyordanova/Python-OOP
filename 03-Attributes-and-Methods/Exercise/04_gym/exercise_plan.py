class ExercisePlan:
    _id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        ExercisePlan._id = ExercisePlan.get_next_id()
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan._id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hour):
        return cls(trainer_id, equipment_id, hour * 60)

    @staticmethod
    def get_next_id():
        return ExercisePlan._id + 1
