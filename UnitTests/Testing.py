""" Scripts to run unit testing"""

import unittest
import sys
from unittest import TestCase

sys.path.append('D:\Things\Github\PokerDesk')
from Table.Deck import Card
    
class Testing(TestCase):
    
    def test_card(self):
        
        from TestCard import TestCard
    
if __name__ == '__main__':
    unittest.main(verbosity = 0, exit = False, catchbreak = True, buffer = True)
# else:
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestSprint1)
#     unittest.TextTestRunner(verbosity = 0).run(suite)
