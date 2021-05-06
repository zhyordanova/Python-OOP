from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:

    @staticmethod
    def increase_beginner_attr(player: Beginner):
        player.health += 40

        for c in player.card_repository.cards:
            c.damage_points += 30

    @staticmethod
    def get_bonus_points(player):
        return sum([c.health_points for c in player.card_repository.cards])

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            self.increase_beginner_attr(attacker)

        if enemy.__class__.__name__ == "Beginner":
            self.increase_beginner_attr(enemy)

        attacker.health += self.get_bonus_points(attacker)
        enemy.health += self.get_bonus_points(enemy)

        for card in attacker.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return

            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return

            attacker.take_damage(card.damage_points)
