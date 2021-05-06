from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    @staticmethod
    def __validate_name(name):
        if name == "":
            raise ValueError("Card cannot be an empty string!")

    def add(self, card: Card):
        names = [c.name for c in self.cards]

        if card.name in names:
            raise ValueError(f"Card {card.name} already exists!")

        self.cards.append(card)
        self.count += 1

    def remove(self, card_name):
        self.__validate_name(card_name)

        card_to_remove = self.find(card_name)
        self.cards.remove(card_to_remove)
        self.count -= 1

    def find(self, name):
        return [c for c in self.cards if c.name == name][0]
