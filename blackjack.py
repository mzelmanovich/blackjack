import random

suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
card_types = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

cards = []
for suit in suits:
    for ctype in card_types:
        cards.append((suit, str(ctype)))

class Deck(object):
    def __init__(this):
        this.cards = cards[:]

    def shuffle(this):
        this.cards = random.sample(this.cards, len(this.cards))

    def draw(this, num=1):
        values = this.cards[:1]
        this.cards = this.cards[1:]

        if len(values) > 0:
            return values

        return None

    def __len__(this):
        return len(this.cards)

    def __iter__(this):
        return this

    def next(this):
        value = this.draw()
        if len(value) > 0:
            return value
        raise StopIteration()

deck = Deck()
print deck.next()
