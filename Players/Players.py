from abc import ABC, abstractmethod
import random

class Player(ABC):
    
    _type = ''
    _hand = []
    
    name = ''
    age = 0
    position = ''
    bankroll = 200000
    
    def __init__(self, name, age, position, bankroll):
            
        self.name = name
        self.age = age
        self.position = position
        self.bankroll = bankroll
    
    def to_check(self):
        pass
        
    def to_fold(self):
        pass
        
    def to_call(self):
        pass
        
    def to_all_in(self):
        pass
         
    def to_raise(self):
        pass
        
    def check_hand(self):
        pass


class Dealer:
    
    _number_of_player = 1
    _deck = None
    
    status = ''
    
    def give_deck(self, deck):
        self._deck = deck
       
    def shuffle(self):
        random.shuffle(self._deck.cards)
        return self._deck
        
    def deal(self):
        pass
    
    def burn_card(self):
        pass
    
    def check(self):
        pass    
        
    def collect_cards(self):
        pass    
        
    def check_number_of_player(self):
        pass    
        
    def __str__(self):
        print(" Dealer is " + str(self.status))
    
    