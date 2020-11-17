import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:
    """
    Contains a list of Card objects, one for each rank/suit combo in a regular 52-card deck
    """
    def __init__(self):
        self.cards = []
        self.get_new_deck()

    def deal(self, num):
        ret = []
        for i in range(num):
            ret.append(self.cards.pop())

        return ret

    def get_new_deck(self):
        self.cards.clear()
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.cards.append(created_card)
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)


class Card:
    """
    Contains the relevant info for a single card in the deck.
    Usable attributes are suit, rank, and value (the numeric equivalent)
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

        self.get_total()

    def clear_cards(self):
        self.hand.clear()

    def get_total(self):
        self.total = 0

        for card in self.hand:
            if card.rank != "Ace":
                self.total += card.value
            else:
                self.total += card.value[0]

        for card in self.hand:
            if card.rank == "Ace":
                if self.total <= 11:
                    self.total -= card.value[0]
                    self.total += card.value[1]

    def print_total(self):
        print(f"{self.name}'s total is {self.total}")
        for i in self.hand:
            print("-----", i, "(", i.value, ")")



