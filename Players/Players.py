import random


list_of_names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Player:
    
    _type = ''
    _hands = []
    
    name = ''
    age = 0
    position = ''
    bankroll = 200000
    
    def __init__(self, name, age, position, bankroll):
            
        self.name = name
        self.age = age
        self.position = position
        self.bankroll = bankroll
    
    def take_card(self, list_cards):
        
        self._hands = list_cards
        
    def to_bet(self, money):
        
        self.bankroll -= money
        
        return 'bet'
        
    def to_check(self):
        
        return 'check'
        
    def to_fold(self):
        
        return 'fold'
        
    def to_call(self, money):
        
        self.bankroll -= money
        
        return 'call'
        
    def to_all_in(self):
        
        all_in_money = self.bankroll
        self.bankroll = 0
        
        return 'all in', all_in_money
         
    def to_raise(self, money):
        
        return 'raise'
        
    def check_hand(self, community_table):
        
        check_cards = []
        check_cards.extend(community_table.show_cards)
        check_cards.extend(self._hands)
        
        number_of_cards = len(check_cards)
        names = []
        suits = []
        result = ()
        
        for i in range(0, number_of_cards):
            card = check_cards[i]
            names.append(card.name)
            suits.append(card.suit)
            
        # Check hands
        is_royal_flush = self.check_royal_flush(check_cards, suits)
        is_flush_straight, flush_straight_value = self.check_flush_straight(check_cards, suits)
        is_four, four_value = self.check_four_of_kind(names)
        is_full_house, full_house_three, full_house_two = self.check_full_house(names)
        is_flush, flush_value, _ = self.check_flush(check_cards, suits)
        is_straight, straight_value = self.check_straight(names)
        is_three, three_value = self.check_three_of_kind(names)
        num_of_pairs, value_1, value_2 = self.check_pairs(names)
        hightest_card = self.get_hightest_card(names)
            
        if is_royal_flush:
            result = ('Royal Flush', None, None)
        elif is_flush_straight:
            result = ('Straight Flush', flush_straight_value, None)
        elif is_four:
            result = ("Four of Kind", four_value, None)
        elif is_full_house:
            result = ("Full House", full_house_three, full_house_two)
        elif is_flush:
            result = ("Flush", flush_value, None)
        elif is_straight:
            result = ("Straight", straight_value, None)
        elif is_three:
            result = ("Three of Kind", three_value, None)
        elif num_of_pairs >= 2:
            result = ("Two Pairs", value_1, value_2)
        elif num_of_pairs == 1:
            result = ("One Pair", value_1, None)
        else:
            result = ("Trash", hightest_card, None)
        
        return result

    @staticmethod
    def check_royal_flush(check_cards, list_suits):
        
        Player.check_flush_straight(check_cards, list_suits)
        
        is_flush_straight, flush_straight_values = Player.check_flush_straight(check_cards, list_suits)
        
        if is_flush_straight and (flush_straight_values == "A"):
            return True
        else:
            return False
        
    @staticmethod
    def check_flush_straight(check_cards, list_suits):
        
        is_flush, _, names = Player.check_flush(check_cards, list_suits)
        if is_flush:
            is_straight, straight_value = Player.check_straight(names)
            if is_straight:
                return True, straight_value
            else:
                return False, None
        else:
            return False, None
        
    @staticmethod
    def check_flush(check_cards, list_suits):
        # Counting
        try: count_S = list_suits.count('S')
        except: count_S = 0
        try: count_C = list_suits.count('C')
        except: count_C = 0
        try: count_D = list_suits.count('D')
        except: count_D = 0
        try: count_H = list_suits.count('H')
        except: count_H = 0
        
        if (count_S >= 5):
            flush_values = []
            flush_names = []
            for card in check_cards:
                if card.suit == 'S':
                    for i in range(0, len(list_of_names)):
                        if card.name == list_of_names[i]:
                            flush_values.append(i)
                            flush_names.append(card.name)
            flush_values.sort()
            flush_value = flush_values[-1]
            return True, list_of_names[flush_value], flush_names
                    
        elif (count_C >= 5):
            flush_values = []
            flush_names = []
            for card in check_cards:
                if card.suit == 'C':
                    for i in range(0, len(list_of_names)):
                        if card.name == list_of_names[i]:
                            flush_values.append(i)
                            flush_names.append(card.name)
            flush_values.sort()
            flush_value = flush_values[-1]
            return True, list_of_names[flush_value], flush_names
            
        elif (count_D >= 5):
            flush_values = []
            flush_names = []
            for card in check_cards:
                if card.suit == 'D':
                    for i in range(0, len(list_of_names)):
                        if card.name == list_of_names[i]:
                            flush_values.append(i)
                            flush_names.append(card.name)
            flush_values.sort()
            flush_value = flush_values[-1]
            return True, list_of_names[flush_value], flush_names
            
        elif (count_H >= 5):
            flush_values = []
            flush_names = []
            for card in check_cards:
                if card.suit == 'H':
                    for i in range(0, len(list_of_names)):
                        if card.name == list_of_names[i]:
                            flush_values.append(i)
                            flush_names.append(card.name)
            flush_values.sort()
            flush_value = flush_values[-1]
            return True, list_of_names[flush_value], flush_names
            
        else:
            return False, None, 'None'

    @staticmethod
    def check_straight(list_names):
        
        # index by names
        indexs = []
        for name in list_names:
            indexs.append(list_of_names.index(name))
        indexs.sort()
        set_index = set(indexs)
        list_index = list(set_index)
        if ((12 in list_index) and (0 in list_index) and (1 in list_index) and (2 in list_index) and (3 in list_index)):
            return True, "5"
        else:
            if len(list_index) == 5:
                if (list_index[-1] - list_index[0] == 4):
                    return True, list_of_names[list_index[-1]]
                else:
                    return False, None
            elif len(list_index) == 6:
                if (list_index[-1] - list_index[1] == 4):
                   return True, list_of_names[list_index[-1]]
                elif (list_index[-2] - list_index[0] == 4):
                   return True, list_of_names[list_index[-2]]
                else:
                    return False, None
            elif len(list_index) == 7:
                if (list_index[-1] - list_index[2] == 4):
                   return True, list_of_names[list_index[-1]]
                elif (list_index[-2] - list_index[1] == 4):
                   return True, list_of_names[list_index[-2]]
                elif (list_index[-3] - list_index[0] == 4):
                   return True, list_of_names[list_index[-3]]
                else:
                    return False, None
            else:
                return False, None
      
    @staticmethod
    def check_four_of_kind(list_names):
        
        for name in list_names:
            if list_names.count(name) == 4:
                return True, name
        
        return False, None
      
    @staticmethod
    def check_full_house(list_names):
        
        is_three, three_value = Player.check_three_of_kind(list_names)
        if is_three:
            num_of_pairs, value_1, value_2 = Player.check_pairs(list_names)
            if num_of_pairs >= 1:
                return True, three_value, value_1
            else:
                return False, None, None
                
        else:
            return False, None, None
      
    @staticmethod
    def check_three_of_kind(list_names):
        
        three_list = []
        set_name = set(list_names)
        for name in set_name:
            if list_names.count(name) == 3:
                three_list.append([name, list_of_names.index(name)])
                
        if len(three_list) == 2:
            if three_list[0][1] > three_list[1][1]:
                return True, three_list[0][0]
            else:
                return True, three_list[1][0]
        elif len(three_list) == 1:
            return True, three_list[0][0]
        else:
            return False, None
      
    @staticmethod
    def check_pairs(list_names):
        
        def filter(key):
            return key[1]

        pair_list = []
        set_name = set(list_names)
        for name in set_name:
            if list_names.count(name) == 2:
                pair_list.append([name, list_of_names.index(name)])
                
        if len(pair_list) > 1:
            pair_list.sort(key = filter)
                
        if len(pair_list) == 0:
            return 0, None, None
        elif len(pair_list) == 1:
            return len(pair_list), pair_list[-1][0], None
        else:
            return len(pair_list), pair_list[-1][0], pair_list[-2][0]
      
    @staticmethod
    def get_hightest_card(list_names):
        
        def filter(key):
            return key[1]

        card_list = []
        set_name = set(list_names)
                
        for name in set_name:
            card_list.append([name, list_of_names.index(name)])
                
        card_list.sort(key = filter)
        
        return card_list[-1][0]
              
    def __str__(self):
        
        return "Player " + str(self.name) + ', '+ str(self.age) + " years old"
    
      
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
    
    