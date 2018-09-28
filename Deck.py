import random as rand
import math
from Card import Card

class Deck:
    """
    Representation of a deck
    Can select if ace is high
    """

    # Initial Init
    # New deck
    def __init__(self):
        self.deck = []
        
        
    # Class Constructors
    # New deck
    def from_new(self, high):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

        # Populates deck
        for rank in range(1 + high, 14 + high):
            for suit in range(0, 4):
                self.deck.append(Card(rank, suits[suit]))
    
    # New deck from input
    def from_input(self, deck_in):
        self.deck = deck_in

    # Adds cards
    def add_cards(self, cards):
        for card in cards:
            self.deck.append(card)

    # Deal a card
    def deal(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card

    # Size of deck
    def size(self):
        return len(self.deck)

    # Shuffle
    def shuffle(self):
        for i in range(0, self.size()):
            temp = self.deck[i]
            num = rand.randint(0, self.size() - 1)
            self.deck[i] = self.deck[num]
            self.deck[num] = temp

    # Prints deck
    def print(self):
        for i in range(0, self.size()):
            self.deck[i].print()

    # Splits deck
    def split(self):
        return self.deck[math.floor(self.size() / 2):self.size()], self.deck[0:math.floor(self.size() / 2)]