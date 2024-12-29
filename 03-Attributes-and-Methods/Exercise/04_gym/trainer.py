class Trainer:
    _id = 0

    def __init__(self, name):
        Trainer._id = Trainer.get_next_id()
        self.name = name
        self.id = Trainer._id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer._id + 1
