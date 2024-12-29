from abc import ABC,abstractmethod

from project.survivor import Survivor


class Medicine(ABC):

    @abstractmethod
    def __init__(self, health_increase: int):
        self.__health_increase = health_increase

    @staticmethod
    def __validate_health_increase(value):
        if value < 0:
            raise ValueError("Health increase cannot be less than zero.")

    @property
    def health_increase(self):
        return self.__health_increase

    @health_increase.setter
    def health_increase(self, value):
        self.__validate_health_increase(value)
        self.__health_increase = value

    def apply(self, survivor: Survivor):
        survivor.health += self.health_increase

