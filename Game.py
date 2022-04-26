"""
    Main table, this is where te game begins
"""


from Table.Deck import *
from Table.Pool import *
from Players.Players import *


# Chose a deck
basic_deck = BasicDeck()
common_cards = CommunityTable()

# Get a dealer
dealer = Dealer()

# Invite players
Phuc = Player('Phuc', 23, 1, 1000000)
Nguyen = Player('Nguyen', 25, 2, 500000)

# Some tests