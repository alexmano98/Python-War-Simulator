# War!!!!
# Simulation made by Alex Manohar
from Player import Player
from Deck import Deck

p1_wins = 0
p2_wins = 0

def win(p1, p2, p1_wins, p2_wins):
    # Check if one player is empty
    if p1.get_deck().size() == 0:
        print(p2.name + " won!")
        p1_wins += 1

    elif p2.get_deck().size() == 0:
        print(p1.name + " won!")
        p2_wins += 1
    elif p1.get_deck().size() == 0 and p2.get_deck().size() == 0:
        print("Tie Game!!!")
    else:
        print("SOMETHING WENT WRONG")

def check_win(p1, p2, p1_wins, p2_wins):
    if p1.get_deck().size() == 0 or p2.get_deck().size() == 0:
        win(p1, p2, p1_wins, p2_wins)
        return True

def comp(c1, c2):
    if c1.get_rank() > c2.get_rank():
        return 1
    if c1.get_rank() < c2.get_rank():
        return 2
    return 0



for x in range(0, 10):
    print(x)
    # Deck stuff
    deck = Deck()
    deck.from_new(0)
    deck.shuffle()
    p1_deck, p2_deck = deck.split()

    # Creates two players
    p1 = Player(p1_deck, "Player 1")
    p2 = Player(p2_deck, "Player 2")

    # Play hand
    done = False
    while not check_win(p1, p2, p1_wins, p2_wins):
    
        pile = []

        # Each player plays a card
        p1_card = p1.play()
        p2_card = p2.play()

        pile.append(p1_card)
        pile.append(p2_card)

        if comp(p1_card, p2_card) == 1:
            p1.won_hand(pile)
        elif comp(p1_card, p2_card) == 2:
            p2.won_hand(pile)

        # War loop
        while p1_card == p2_card:

            # Check if one player is empty
            if check_win(p1, p2, p1_wins, p2_wins):
                done = True
                break

            p1.play()
            p2.play()

            pile.append(p1_card)
            pile.append(p2_card)

            # Check if one player is empty
            if check_win(p1, p2, p1_wins, p2_wins):
                done = True
                break

            # Each player plays a card
            p1_card = p1.play()
            p2_card = p2.play()

            pile.append(p1_card)
            pile.append(p2_card)

            if comp(p1_card, p2_card) == 1:
                p1.won_hand(pile)
            elif comp(p1_card, p2_card) == 2:
                p2.won_hand(pile)

        if done:
            break
    if p1.deck.size() == 0:
        p2_wins += 1
    else:
        p1_wins += 1

print("Player 1 wins: ", p1_wins)
print("Player 2 wins: ", p2_wins)