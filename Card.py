class Card:
    """
    Representation of a card
    Each card has a rank and suit
    Suit in format of "Spades, Hearts, Diamonds, Clubs"
    Rank can be 1-13 (2-14 if ace is high)
    """
    # Init
    def __init__(self, rank_in, suit_in):
        self.rank = rank_in
        self.suit = suit_in

    # Get rank
    def get_rank(self):
        return self.rank

    # Get suit
    def get_suit(self):
        return self.suit

    # Print card
    def print(self):
        rk = ""
        if(self.rank == 1 or self.rank == 14):
            rk = "Ace"
        elif(self.rank == 11):
            rk = "Jack"
        elif(self.rank == 12):
            rk = "Queen"
        elif(self.rank == 13):
            rank = "King"

        if(self.rank == 1 or (self.rank > 10 and self.rank <= 14)):
            print(rk, " of ", self.suit)
        else:
            print(self.rank, " of ", self.suit)

    # Compare card
    def __eq__(self, other):
        return self.rank == other.rank
