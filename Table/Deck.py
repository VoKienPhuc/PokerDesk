from abc import ABC, abstractmethod

names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
name_call = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
             'Ten', 'Jack', 'Queen', 'King', 'Ace']
suits = ['S', 'C', 'D', 'H']
 
    
class Card:
    
    name = ''
    suit = ''
    
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        
    def __str__(self):
        
        # Looking for name_call
        index = 0
        index = names.index(self.name)
        name = name_call[index]
        
        # Looking for Suit
        if self.suit == 'S':
            suit = 'Spade'
        elif self.suit == 'C':
            suit = 'Club'
        elif self.suit == 'D':
            suit = 'Diamond'
        else:
            suit = 'Heart'
            
        return "The {} of {}".format(name, suit)
        

class Deck(ABC):
    
    number_of_card = 0
    cards = []
    

class BasicDeck(Deck):
    
    number_of_card = 52
    cards = []
    
    for name in names:
        for suit in suits:
            card = Card(name, suit)
            cards.append(card)
 

class CommunityCards:
    
    number_of_opencard = 0
    _cards = []
    show_cards = []
    
    def check_showed_cards(self):
        pass
        
    def show_a_card(self):
        pass
        
    def add_cards(self, cards):
        self._cards = cards