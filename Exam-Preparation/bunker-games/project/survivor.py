class Survivor:
    MAX_HEALTH = 100
    MAX_NEEDS = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = Survivor.MAX_HEALTH
        self.needs = Survivor.MAX_NEEDS

    @staticmethod
    def __validate_name(value):
        if value == '':
            raise ValueError("Name not valid!")

    @staticmethod
    def __validate_age(value):
        if value < 0:
            raise ValueError("Age not valid!")

    @staticmethod
    def __validate_health(value):
        if value < 0:
            raise ValueError("Health not valid!")

    @staticmethod
    def __validate_needs(value):
        if value < 0:
            raise ValueError("Needs not valid!")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self._age = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self.__validate_health(value)
        if value > Survivor.MAX_HEALTH:
            self._health = Survivor.MAX_HEALTH
            return
        self._health = value

    @property
    def needs(self):
        return self._needs

    @needs.setter
    def needs(self, value):
        self.__validate_needs(value)
        if value > Survivor.MAX_NEEDS:
            self._needs = Survivor.MAX_NEEDS
            return
        self._needs = value

    @property
    def needs_sustenance(self):
        return True if self.needs < Survivor.MAX_NEEDS else False

    @property
    def needs_healing(self):
        return True if self.health < Survivor.MAX_HEALTH else False
