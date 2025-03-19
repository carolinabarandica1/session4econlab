class Card:
    ranks = ['2','3','4','5','6','7','8','9','10',
             'J', 'Q', 'K','A']
    suits = ['♠', '♥', '♦', '♣']
    def __init__(self, suit, rank):
        if rank not in self.ranks:
            raise ValueError('invalid rank')
        if suit not in self.suits:
            raise ValueError('invalid suit')
        self._suit = suit
        self._rank = rank

    def __str__(self):
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        return self.__str__()

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        self._suit = value

    @property
    def rank(self):
        return self.rank

    @rank.setter
    def rank(self):
        return self.rank


class Deck:
    def __init__(self):
        self._deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self._deck.append(Card(suit,rank))

    def __str__(self):
        return str(self._deck)

jack_clubs= Card('♠', 'J')
print(jack_clubs)