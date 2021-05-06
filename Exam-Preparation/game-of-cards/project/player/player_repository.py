from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    @staticmethod
    def __validate_name(name):
        if name == "":
            raise ValueError("Player cannot be an empty string!")

    @property
    def player_count(self):
        return len(self.players)

    def add(self, player: Player):
        names = [p.username for p in self.players]

        if player.username in names:
            raise ValueError(f"Player {player.username} already exists!")

        self.players.append(player)
        self.count = self.player_count

    def remove(self, player_name):
        self.__validate_name(player_name)

        player_to_remove = self.find(player_name)
        self.players.remove(player_to_remove)
        self.count = self.player_count

    def find(self, username):
        return [p for p in self.players if p.username == username][0]
