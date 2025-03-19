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

jack_clubs= Card('♠', 'J')
print(jack_clubs)