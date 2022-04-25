""" Scripts to run unit testing"""

import sys
sys.path.append('D:\Things\Github\PokerDesk')

import unittest
from unittest import TestCase

from UnitTests.TestCard import *
    
class Testing(TestCase):
    
    def test_card(self):
        
        pass
        # from TestCard import TestCard
        # from TestCard import TestDeck
    
if __name__ == '__main__':
    unittest.main(verbosity = 2, exit = False, catchbreak = True, buffer = True)
