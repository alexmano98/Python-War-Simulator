from Deck import Deck

class Player:
    """
    Each player has a deck containing a current deck and a won deck
    """

    # Init
    def __init__(self, deck_in, name_in):
        self.name = name_in
        self.deck = Deck()
        self.deck.from_input(deck_in)

    # Plays a card
    def play(self):
        #print(self.name, " plays ", end = '')
        card = self.deck.deal()
        #card.print()
        return card

    def won_hand(self, cards):
        self.deck.add_cards(cards)

    def get_deck(self):
        return self.deck