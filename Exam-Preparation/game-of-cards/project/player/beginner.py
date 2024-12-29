from project.player.player import Player


class Beginner(Player):
    initial_health = 50

    def __init__(self, username):
        super().__init__(username, self.initial_health)
