
import sys
from unittest import TestCase

sys.path.append('D:\Things\Github\PokerDesk')
from Table.Deck import Card, BasicDeck, CommunityTable
    
class TestCard(TestCase):
    
    def test_value(self):
        
        data = [('2', 'S', "The Two of Spade"),
                ('4', 'H', "The Four of Heart"),
                ('8', 'C', "The Eight of Club"),
                ('6', 'S', "The Six of Spade"),
                ('Q', 'D', "The Queen of Diamond"),
                ('3', 'H', "The Three of Heart"),
                ('10', 'D', "The Ten of Diamond"),
                ('K', 'H', "The King of Heart"),
                ('A', 'C', "The Ace of Club"),
                ('J', 'S', "The Jack of Spade")]
        
        for i in range(0, len(data)):
            card = Card(data[i][0], data[i][1])
            self.assertEqual(card.__str__(), data[i][2])
   
    
class TestDeck(TestCase):
    
    def test_add_card(self):
        
        data = [('2', 'S', "The Two of Spade"),
                ('4', 'H', "The Four of Heart"),
                ('8', 'C', "The Eight of Club"),
                ('6', 'S', "The Six of Spade"),
                ('Q', 'D', "The Queen of Diamond"),
                ('3', 'H', "The Three of Heart"),
                ('10', 'D', "The Ten of Diamond"),
                ('K', 'H', "The King of Heart"),
                ('A', 'C', "The Ace of Club"),
                ('J', 'S', "The Jack of Spade")]
        
        for i in range(0, len(data)):
            card = Card(data[i][0], data[i][1])
            basic_deck = BasicDeck()
            basic_deck.add_card(card)
            self.assertEqual(basic_deck._cards[-1].__str__(), data[i][2])
   
    def test_get_random_card(self):
        
        for _ in range(0, 20):
            basic_deck_rand = BasicDeck()
            basic_deck_rand.get_random_card()
   
    def test_get_card(self):
        
        data = [('2', 'S', "The Two of Spade"),
                ('4', 'H', "The Four of Heart"),
                ('8', 'C', "The Eight of Club"),
                ('6', 'S', "The Six of Spade"),
                ('Q', 'D', "The Queen of Diamond"),
                ('3', 'H', "The Three of Heart"),
                ('10', 'D', "The Ten of Diamond"),
                ('K', 'H', "The King of Heart"),
                ('A', 'F', 'None'),
                ('J', '1', 'None')]
        
        basic_deck = BasicDeck()
        for i in range(0, len(data)):
            basic_deck.reset()
            card = basic_deck.get_card(data[i][0], data[i][1])
            self.assertEqual(card.__str__(), data[i][2])
   
    def test_looking_for_card(self):
        
        data = [('2', 'S', 0),
                ('4', 'H', 11),
                ('8', 'C', 25),
                ('6', 'S', 16),
                ('Q', 'D', 42),
                ('3', 'H', 7),
                ('10', 'D', 34),
                ('11', 'H', None),
                ('1', 'C', None),
                ('S', 'S', None)]
        
        basic_deck = BasicDeck()
        for index in range(0, len(data)):
            basic_deck.reset()
            self.assertEqual(basic_deck.looking_for_card(data[index][0], data[index][1]), data[index][2])
   
    def test_get_number(self):
        
        data = [(1, 51),
                (4, 48),
                (2, 50),
                (3, 49),
                (8, 44),
                (52, 0),
                (0, 52),
                (30, 22)]
        
        basic_deck = BasicDeck()
        for i in range(0, len(data)):
            basic_deck.reset()
            basic_deck.get_top_cards(data[i][0])
            self.assertEqual(basic_deck.get_number(), data[i][1])
   
    def test_get_top_cards(self):
        
        data = [(3, 3, 49),
                (5, 5, 47),
                (1, 1, 51),
                (12, 12, 40),
                (22, 22, 30),
                (31, 31, 21),
                (-5, 0, 52),
                (53, 0, 52),
                ('s', 0, 52),
                ("", 0, 52)]
        
        basic_deck = BasicDeck()
        
        for i in range(0, len(data)):
            basic_deck.reset()
            list_card = basic_deck.get_top_cards(data[i][0])
            self.assertEqual(len(list_card), data[i][1])
            self.assertEqual(basic_deck.number_of_card, data[i][2])
   
    def test_get_bottom_cards(self):
        
        data = [(3, 3, 49),
                (5, 5, 47),
                (1, 1, 51),
                (12, 12, 40),
                (22, 22, 30),
                (31, 31, 21),
                (-5, 0, 52),
                (53, 0, 52),
                ('s', 0, 52),
                ("", 0, 52)]
        
        basic_deck = BasicDeck()
        
        for i in range(0, len(data)):
            basic_deck.reset()
            list_card = basic_deck.get_bottom_cards(data[i][0])
            self.assertEqual(len(list_card), data[i][1])
            self.assertEqual(basic_deck.number_of_card, data[i][2])
   
    
class TestCommunityTable(TestCase):
    
    def test_check_showed_cards(self):
        
        data = [('2', 'S', "The Two of Spade"),
                ('4', 'H', "The Four of Heart"),
                ('8', 'C', "The Eight of Club"),
                ('6', 'S', "The Six of Spade"),
                ('Q', 'D', "The Queen of Diamond")]
        
        testing = [(3, 3),
                   (2, 2),
                   (1, 1),
                   (4, 4),
                   (0, 0),
                   (5, 5),
                   (9, 0),
                   (-4, 0)]
        
        list_cards = []
        for i in range(0, len(data)):
            card = Card(data[i][0], data[i][1])
            list_cards.append(card)
            
        table = CommunityTable()
        for i in range(0, len(testing)):
            table.set_cards(list_cards)
            table.show_card(testing[i][0])
            self.assertEqual(len(table.check_showed_cards()), testing[i][1])
   
    def test_show_card(self):
        
        data = [('2', 'S', "The Two of Spade"),
                ('4', 'H', "The Four of Heart"),
                ('8', 'C', "The Eight of Club"),
                ('6', 'S', "The Six of Spade"),
                ('Q', 'D', "The Queen of Diamond")]
        
        testing = [(3, 3),
                   (2, 2),
                   (1, 1),
                   (4, 4),
                   (0, 0),
                   (5, 5),
                   (9, 0),
                   (-4, 0)]
        
        list_cards = []
        for i in range(0, len(data)):
            card = Card(data[i][0], data[i][1])
            list_cards.append(card)
            
        table = CommunityTable()
        for i in range(0, len(testing)):
            table.set_cards(list_cards)
            table.show_card(testing[i][0])
            self.assertEqual(len(table.show_cards), testing[i][1])
   
    def test_add_cards(self):
        
        data = [('2', 'S', "The Two of Spade"),
                ('4', 'H', "The Four of Heart"),
                ('8', 'C', "The Eight of Club"),
                ('6', 'S', "The Six of Spade"),
                ('Q', 'D', "The Queen of Diamond"),
                ('3', 'H', "The Three of Heart"),
                ('10', 'D', "The Ten of Diamond"),
                ('K', 'H', "The King of Heart"),
                ('A', 'F', 'The Ace of None'),
                ('J', '1', 'The Jack of None')]
        
        table = CommunityTable()
        for i in range(0, len(data)):
            table.reset()
            card = Card(data[i][0], data[i][1])
            table.set_cards([card])
            self.assertEqual(table._cards[0].__str__(), data[i][2])
   
    