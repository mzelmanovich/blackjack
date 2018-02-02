import random

suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
card_types = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
suit_name_values = {}
card_type_values = {}
cards = []

# Lets set up the dictionaries and set deck of cards
for i,suit in enumerate(suits):
    suit_name_values[suit] = i
    for j,ctype in enumerate(card_types):
        cards.append((suit, str(ctype)))

        if len(cards) != len (card_types):
            card_type_values[str(ctype)] = j + 1

def get_value(suit, ctype):
    val = int(card_type_values[ctype])
    if val > 10:
        return 10
    return 10

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
print suit_name_values
print card_type_values
