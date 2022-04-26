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
    _community_table = None
    
    status = 'Ready'
    
    def set_deck(self, deck):
        self._deck = deck
       
    def set_community_table(self, community_table):
        
        self._community_table = community_table
        
    def set_number_of_player(self, number):
        
        self._number_of_player = abs(number)
        
    def shuffle(self):
        random.shuffle(self._deck._cards)
        return self._deck
        
    def draw(self, number_of_card):
        
        list_cards = self._deck.get_top_cards(number_of_card)
        return list_cards
    
    def deal(self):
        
        list_of_cards = []
        
        if self._number_of_player <= 10:
            
            for _ in range(0, self._number_of_player):
                list_of_cards.append(self.draw(2))
                
        commnity_cards = self.draw(5)
        self._community_table.set_cards(commnity_cards)
        list_of_cards.append(commnity_cards)
            
        return list_of_cards
    
    def check(self):
        
        number_of_showed_card = len(self._community_table.show_cards)
        if number_of_showed_card == 0:
            self._community_table.show_card(3)
        elif number_of_showed_card == 3:
            self._community_table.show_card(1)
        elif number_of_showed_card == 4:
            self._community_table.show_card(1)
        
    def collect_cards(self):
        
        self._deck.reset()
        self._community_table.reset() 
        
    def __str__(self):
        
        return "Dealer is " + str(self.status)
    
    