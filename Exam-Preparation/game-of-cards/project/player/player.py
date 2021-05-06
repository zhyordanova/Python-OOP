from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):

    @abstractmethod
    def __init__(self, username: str, health: int):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @staticmethod
    def __validate_name(value):
        if value == '':
            raise ValueError("Player's username cannot be an empty string.")

    @staticmethod
    def __validate_value(value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")

    @staticmethod
    def __validate_damage_points(points):
        if points < 0:
            raise ValueError("Damage points cannot be less than zero.")

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_name(value)
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__validate_value(value)
        self.__health = value

    @property
    def is_dead(self):
        return True if self.health <= 0 else False

    def take_damage(self, damage_points: int):
        self.__validate_damage_points(damage_points)
        self.health -= damage_points
