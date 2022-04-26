""" Scripts to run unit testing"""

import sys
sys.path.append('D:\Things\Github\PokerDesk')

import unittest

from UnitTests.TestCard import TestCard
from UnitTests.TestCard import TestDeck
from UnitTests.TestCard import TestCommunityTable
from UnitTests.TestPlayers import TestDealer

if __name__ == '__main__':
    unittest.main(verbosity = 2, exit = False, catchbreak = True, buffer = True)
