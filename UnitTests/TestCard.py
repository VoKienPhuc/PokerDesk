
import sys
from unittest import TestCase

sys.path.append('D:\Things\Github\PokerDesk')
from Table.Deck import Card
    
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
    