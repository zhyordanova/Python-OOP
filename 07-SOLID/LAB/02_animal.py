from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def get_sound(self):
        pass


class Cat(Animal):
    sound = 'meow'

    def get_sound(self):
        return self.sound


class Dog(Animal):
    sound = 'woof-woof'

    def get_sound(self):
        return self.sound


def animal_sound(animals):
    for animal in animals:
        print(animal.get_sound())



animals = [Cat(), Dog()]
animal_sound(animals)

