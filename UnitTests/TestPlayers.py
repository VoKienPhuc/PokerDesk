import sys
from unittest import TestCase

sys.path.append('D:\Things\Github\PokerDesk')
from Table.Deck import BasicDeck, CommunityTable
from Players.Players import Dealer
    
class TestDealer(TestCase):
    
    def test_shuffle(self):
        
        basic_deck = BasicDeck()
        dealer = Dealer()
        dealer.set_deck(basic_deck)
        
        data = ([0, "The Two of Spade"],
                [11, "The Four of Heart"],
                [25, "The Eight of Club"],
                [42, "The Queen of Diamond"])
        
        for _ in range(0, 10):
            dealer.shuffle()
            list_check = []
            for i in range(0, len(data)):
                if dealer._deck._cards[data[i][0]].__str__() != data[i][1]:
                    list_check.append(True)
                else:
                    list_check.append(False)
            result = list_check[0] or list_check[1] or list_check[2] or list_check[3]
            self.assertTrue(result)
   
    def test_draw(self):
        
        basic_deck = BasicDeck()
        dealer = Dealer()
        community_table = CommunityTable()
        dealer.set_deck(basic_deck)
        dealer.set_community_table(community_table)
        
        testing = [(3, 3),
                   (22, 22),
                   (15, 15),
                   (41, 41),
                   (33, 33),
                   (55, 0),
                   (0, 0),
                   (-4, 0)]
        
        for i in range(0, len(testing)):
            dealer.collect_cards()
            dealer.draw(testing[i][0])
            self.assertEqual(len(dealer._deck._cards), 52-testing[i][1])
   
    def test_check(self):
        
        basic_deck = BasicDeck()
        dealer = Dealer()
        community_table = CommunityTable()
        dealer.set_deck(basic_deck)
        dealer.set_community_table(community_table)
        dealer._community_table.set_cards(dealer.draw(5))
        
        for i in range(0, 3):
            dealer.check()
            if i == 0:
                self.assertEqual(len(dealer._community_table.check_showed_cards()), 3)
            elif i == 1:
                self.assertEqual(len(dealer._community_table.check_showed_cards()), 4)
            elif i == 2:
                self.assertEqual(len(dealer._community_table.check_showed_cards()), 5)

    def test_deal(self):
        
        basic_deck = BasicDeck()
        community_table = CommunityTable()
        dealer = Dealer()
        dealer.set_deck(basic_deck)
        dealer.set_community_table(community_table)
        
        data1 = [(2, 3),
                 (0, 1),
                 (5, 6),
                 (-5, 6),
                 (11, 1),
                 (31, 1)]
        
        for i in range(0, len(data1)):
            dealer.set_number_of_player(data1[i][0])
            dealer.collect_cards()
            big_list = dealer.deal()
            self.assertEqual(len(big_list), data1[i][1])
        