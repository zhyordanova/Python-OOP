from abc import ABC, abstractmethod

from project.survivor import Survivor


class Supply(ABC):

    @abstractmethod
    def __init__(self, needs_increase: int):
        self.__needs_increase = needs_increase

    @staticmethod
    def __validate_needs_increase(value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")

    @property
    def needs_increase(self):
        return self.__needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        self.__validate_needs_increase(value)
        self.__needs_increase = value

    def apply(self, survivor: Survivor):
        survivor.needs += self.needs_increase
