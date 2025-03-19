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

    @property
    def is_flush(self):
        for card in self._cards[1:]:
            if self._cards[0].suit != card.suit:
                return False
        return True

    def __str__(self):
        return str(self._cards)


deck = Deck()
deck.shuffle()

hand = PokerHand(deck)
print(hand)

count = 0
flushes = 0

while True:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_flush:
        flushes += 1
        print(f'probability of a flush is {100*flushes/count}%')
        print(hand)
        break
    count += 1

