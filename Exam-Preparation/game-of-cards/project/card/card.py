from abc import ABC, abstractmethod


class Card(ABC):

    @abstractmethod
    def __init__(self, name: str, damage_points: int, health_points: int):
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points

    @staticmethod
    def __validate_name(value):
        if value == '':
            raise ValueError("Card's name cannot be an empty string.")

    @staticmethod
    def __validate_damage_points(value):
        if value < 0:
            raise ValueError("Card's damage points cannot be less than zero.")

    @staticmethod
    def __validate_health_points(value):
        if value < 0:
            raise ValueError("Card's HP cannot be less than zero.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def damage_points(self):
        return self.__damage_points

    @damage_points.setter
    def damage_points(self, value):
        self.__validate_damage_points(value)
        self.__damage_points = value

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        self.__validate_health_points(value)
        self.__health_points = value
