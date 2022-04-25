from abc import ABC, abstractmethod
import random
from typing import overload

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
    _cards = []
    
    @abstractmethod
    def reset(self):
        pass
    
    # Add a card to deck
    def add_card(self, card):
        
        if isinstance(card, Card):
           self._cards.append(card)
        else:
            print("This is not a Card object")
    
    # Get a random card
    def get_random_card(self):
        
        index = random.randint(0, len(self._cards) - 1)
        
        card = self._cards.pop(index)
        self.number_of_card = len(self._cards)
        
        return card
    
    # Get card by name and suit
    def get_card(self, name: str, suit: str):
        
        # looking for the card
        index = self.looking_for_card(name, suit)
        
        if isinstance(index, int):
            card = self._cards.pop(index)
            self.number_of_card = self.number_of_card - 1
            return card
        else:
            return None
        
    # Get some cards on top of deck
    def get_top_cards(self, number: int):
        
        if not isinstance(number, int):
            return []
        else:
            if number > len(self._cards):
                return []
            elif number < 0:
                return []
            else:
                drawn_cards = []
                
                for _ in range(0, number):
                    drawn_cards.append(self._cards.pop(0))
                    
                self.number_of_card = len(self._cards)
                
                return drawn_cards
            
    # Get some cards at the bottom of deck
    def get_bottom_cards(self, number: int):
        
        if not isinstance(number, int):
            return []
        else:
            if number > len(self._cards):
                return []
            elif number < 0:
                return []
            else:
                drawn_cards = []
                
                for _ in range(0, number):
                    drawn_cards.append(self._cards.pop(-1))
                    
                self.number_of_card = len(self._cards)
                
                return drawn_cards
    
    # Get number of cards in the deck    
    def get_number(self):
        
        self.number_of_card = len(self._cards)
        
        return self.number_of_card
    
    # Looking for a specific card (from 0)
    def looking_for_card(self, name: str, suit: str):
        
        for index in range(0, len(self._cards)):
            if (name == self._cards[index].name) and (suit == self._cards[index].suit):
                return index
            
        return None
                    

class BasicDeck(Deck):
    
    number_of_card = 52
    _cards = []
    
    for name in names:
        for suit in suits:
            card = Card(name, suit)
            _cards.append(card)
 
    def reset(self):
        
        self.number_of_card = 52
        self._cards = []
        
        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self._cards.append(card)
    

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