from deck import Deck, Card


class PokerHand:
    def __init__(self, deck):
        cards = []
        for i in range(10):
            cards.append(deck.draw())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = value

    def __str__(self):
        return str(self._cards)


deck = Deck()
deck.shuffle()

hand = PokerHand(deck)
print(hand)
