import sys
from unittest import TestCase

sys.path.append('D:\Things\Github\PokerDesk')
from Table.Deck import BasicDeck, Card, CommunityTable
from Players.Players import Dealer, Player
    
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
        
class TestPlayer(TestCase):
    
    def test_create_player(self):
        
        data = (['Phuc', 22, "Player Phuc, 22 years old"],
                ['Nguyen', 25,  "Player Nguyen, 25 years old"],
                ['Tien', 24,  "Player Tien, 24 years old"],
                ['Daniel', 90,  "Player Daniel, 90 years old"],
                ['Özil', 35,  "Player Özil, 35 years old"],
                ['Unknown', 99,  "Player Unknown, 99 years old"],
                [997, '0',  "Player 997, 0 years old"],
                [1999, 'VKP',  "Player 1999, VKP years old"])
        
        for i in range(len(data)):
            player = Player(data[i][0], data[i][1], 0, 50000)
            self.assertEqual(player.__str__(), data[i][2])
    
    def test_check_royal_flush(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','S'], ['A','S'], True],
                [['10','D'], ['J','D'], ['Q','D'], ['K','D'], ['A','D'], True],
                [['10','C'], ['J','C'], ['Q','C'], ['K','C'], ['A','C'], True],
                [['10','H'], ['J','H'], ['Q','H'], ['K','H'], ['A','H'], True],
                [['10','H'], ['J','H'], ['Q','H'], ['K','H'], ['A','H'], ['A','C'], True],
                [['10','H'], ['J','H'], ['Q','H'], ['K','H'], ['5','H'], ['A','H'], True],
                [['10','H'], ['J','H'], ['Q','H'], ['K','S'], ['K','H'], ['A','H'], True],
                [['10','D'], ['J','H'], ['Q','H'], ['K','H'], ['10','H'], ['A','H'], True],
                [['9','D'], ['J','D'], ['Q','D'], ['K','D'], ['A','D'], False],
                [['10','D'], ['J','D'], ['Q','D'], ['K','D'], ['2','D'], False],
                [['10','D'], ['J','D'], ['Q','D'], ['K','D'], ['A','S'], False],
                [['10','D'], ['J','D'], ['Q','H'], ['K','D'], ['A','D'], False],
                [['10','D'], ['J','C'], ['Q','D'], ['K','C'], ['A','D'], False],
                [['10','D'], ['J','C'], ['Q','D'], ['K','C'], ['A','D'], ['A','C'], ['A','S'], False])
        
        for i in range(len(data)):
            check_cards = []
            suits = []
            for j in range(len(data[i])-1):
                check_cards.append(Card(data[i][j][0], data[i][j][1]))
            for index in range(0, len(check_cards)):
                card = check_cards[index]
                suits.append(card.suit)
            self.assertEqual(Player.check_royal_flush(check_cards, suits), data[i][-1], "==> Data "+str(i))
    
    def test_check_flush_straight(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','C'], ['A','S'], [False, None]],
                [['J','D'], ['J','D'], ['Q','D'], ['J','H'], ['3','D'], [False, None]],
                [['Q','D'], ['2','D'], ['5','D'], ['4','D'], ['K','H'], ['7','D'], [False, None]],
                [['3','H'], ['7','H'], ['Q','H'], ['2','H'], ['A','H'], [False, None]],
                [['10','H'], ['J','C'], ['Q','D'], ['K','D'], ['9','C'], ['A','C'], [False, None]],
                [['10','H'], ['9','C'], ['8','D'], ['7','D'], ['5','C'], ['J','H'], [False, None]],
                [['4','S'], ['9','S'], ['10','S'], ['K','S'], ['Q','S'], ['J','S'], [True, 'K']],
                [['A','D'], ['9','H'], ['8','H'], ['7','H'], ['2','S'], ['6','H'], ['10','H'], [True, '10']],
                [['4','H'], ['8','D'], ['5','H'], ['10','D'], ['7','H'], ['8','H'], ['6','H'], [True, '8']],
                [['A','S'], ['4','S'], ['5','S'], ['3','S'], ['Q','S'], ['2','S'], ['K','S'], [True, '5']],
                [['9','D'], ['J','D'], ['3','H'], ['K','D'], ['Q','D'], ['10','D'], [True, 'K']])
        
        for i in range(len(data)):
            check_cards = []
            suits = []
            for j in range(len(data[i])-1):
                check_cards.append(Card(data[i][j][0], data[i][j][1]))
            for index in range(0, len(check_cards)):
                card = check_cards[index]
                suits.append(card.suit)
            num, value = Player.check_flush_straight(check_cards, suits)
            self.assertEqual(num, data[i][-1][0], "→ Data " + str(i))
            self.assertEqual(value, data[i][-1][1], "→ Data " + str(i))
     
    def test_check_flush(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','C'], ['A','S'], [False, None]],
                [['J','D'], ['J','D'], ['Q','D'], ['J','H'], ['3','D'], [False, None]],
                [['5','S'], ['5','C'], ['5','D'], ['4','H'], [False, None]],
                [['3','H'], ['3','H'], ['Q','H'], ['2','S'], ['A','H'], [False, None]],
                [['10','H'], ['K','C'], ['Q','D'], ['K','D'], ['10','C'], ['3','C'], [False, None]],
                [['10','H'], ['10','C'], ['5','D'], ['10','D'], ['5','C'], [False, None]],
                [['4','S'], ['9','S'], ['10','S'], ['K','S'], ['Q','S'], ['J','H'], [True, 'K']],
                [['A','D'], ['9','H'], ['8','H'], ['7','H'], ['2','S'], ['2','H'], ['10','H'], [True, '10']],
                [['5','H'], ['8','D'], ['2','H'], ['10','D'], ['7','H'], ['8','H'], ['3','H'], [True, '8']],
                [['4','S'], ['9','S'], ['10','S'], ['3','S'], ['Q','S'], ['A','S'], ['K','S'], [True, 'A']],
                [['4','D'], ['8','D'], ['3','H'], ['K','D'], ['Q','D'], ['10','D'], [True, 'K']])
        
        for i in range(len(data)):
            check_cards = []
            suits = []
            for j in range(len(data[i])-1):
                check_cards.append(Card(data[i][j][0], data[i][j][1]))
            for index in range(0, len(check_cards)):
                card = check_cards[index]
                suits.append(card.suit)
            num, value, _ = Player.check_flush(check_cards, suits)
            self.assertEqual(num, data[i][-1][0], "→ Data " + str(i))
            self.assertEqual(value, data[i][-1][1], "→ Data " + str(i))
    
    def test_check_straight(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','S'], ['A','S'], [True, 'A']],
                [['J','D'], ['J','D'], ['Q','D'], ['J','D'], ['3','D'], [False, None]],
                [['5','S'], ['5','C'], ['5','D'], ['4','H'], [False, None]],
                [['3','H'], ['3','H'], ['Q','H'], ['2','H'], ['A','H'], [False, None]],
                [['10','H'], ['K','C'], ['Q','D'], ['K','D'], ['10','C'], ['3','C'], [False, None]],
                [['10','H'], ['10','C'], ['5','D'], ['10','D'], ['5','C'], [False, None]],
                [['4','D'], ['9','C'], ['10','H'], ['K','S'], ['Q','D'], ['J','H'], [True, 'K']],
                [['A','D'], ['9','D'], ['8','C'], ['7','D'], ['5','S'], ['6','H'], ['10','H'], [True, '10']],
                [['5','S'], ['8','D'], ['4','C'], ['6','D'], ['7','S'], ['8','H'], [True, '8']])
        
        for i in range(len(data)):
            check_cards = []
            names = []
            for j in range(len(data[i])-1):
                check_cards.append(Card(data[i][j][0], data[i][j][1]))
            for index in range(0, len(check_cards)):
                card = check_cards[index]
                names.append(card.name)
            print(data[i])
            print(names)
            print(type(names))
            num, high1 = Player.check_straight(names)
            self.assertEqual(num, data[i][-1][0], "→ Data " + str(i))
            self.assertEqual(high1, data[i][-1][1], "→ Data " + str(i))
    
    def test_check_four_of_kind(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','S'], ['A','S'], [False, None]],
                [['J','D'], ['J','D'], ['Q','D'], ['J','D'], ['3','D'], [False, None]],
                [['5','S'], ['5','C'], ['5','D'], ['4','H'], [False, None]],
                [['3','H'], ['3','H'], ['Q','H'], ['2','H'], ['A','H'], [False, None]],
                [['10','H'], ['10','C'], ['5','D'], ['10','D'], ['5','C'], [False, None]],
                [['10','C'], ['K','H'], ['Q','S'], ['K','D'], ['3','H'], ['6','C'], [False, None]],
                [['4','D'], ['K','C'], ['4','H'], ['K','S'], ['K','D'], ['K','H'], [True, 'K']],
                [['A','D'], ['A','S'], ['2','C'], ['A','C'], ['A','H'], [True, 'A']],
                [['A','D'], ['2','D'], ['2','C'], ['4','D'], ['2','S'], ['2','H'], ['4','H'], [True, '2']],
                [['10','S'], ['2','D'], ['10','C'], ['10','D'], ['Q','S'], ['10','H'], [True, '10']])
        
        for i in range(len(data)):
            check_cards = []
            names = []
            for j in range(len(data[i])-1):
                check_cards.append(Card(data[i][j][0], data[i][j][1]))
            for index in range(0, len(check_cards)):
                card = check_cards[index]
                names.append(card.name)
            num, high1 = Player.check_four_of_kind(names)
            self.assertEqual(num, data[i][-1][0], "→ Data " + str(i))
            self.assertEqual(high1, data[i][-1][1], "→ Data " + str(i))
    
    def test_check_full_house(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','S'], ['A','S'], [False, None, None]],
                [['J','D'], ['J','D'], ['Q','D'], ['J','D'], ['3','D'], [False, None, None]],
                [['5','S'], ['5','C'], ['5','D'], ['5','H'], [False, None, None]],
                [['3','H'], ['3','S'], ['3','C'], ['A','C'], ['A','D'], ['A','H'], [False, None, None]],
                [['10','H'], ['10','C'], ['5','D'], ['10','D'], ['10','S'], ['5','C'], [False, None, None]],
                [['10','C'], ['K','H'], ['K','S'], ['K','D'], ['3','H'], ['6','C'], [False, None, None]],
                [['4','D'], ['4','C'], ['2','H'], ['K','S'], ['K','D'], ['K','H'], [True, 'K', '4']],
                [['A','D'], ['7','D'], ['7','C'], ['A','C'], ['A','H'], [True, 'A', '7']],
                [['A','D'], ['2','D'], ['2','C'], ['Q','D'], ['2','S'], ['Q','H'], [True, '2', 'Q']],
                [['6','H'], ['2','D'], ['2','C'], ['6','D'], ['6','S'], ['Q','H'], [True, '6', '2']],
                [['4','S'], ['8','C'], ['8','D'], ['4','C'], ['5','D'], ['8','S'], ['5','H'], [True, '8', '5']],
                [['J','S'], ['J','C'], ['J','D'], ['A','C'], ['A','D'], ['10','S'], ['10','H'], [True, 'J', 'A']])
        
        for i in range(len(data)):
            check_cards = []
            names = []
            for j in range(len(data[i])-1):
                check_cards.append(Card(data[i][j][0], data[i][j][1]))
            for index in range(0, len(check_cards)):
                card = check_cards[index]
                names.append(card.name)
            num, high1, high2 = Player.check_full_house(names)
            self.assertEqual(num, data[i][-1][0], "→ Data " + str(i))
            self.assertEqual(high1, data[i][-1][1], "→ Data " + str(i))
            self.assertEqual(high2, data[i][-1][2], "→ Data " + str(i))
    
    def test_check_three_of_kind(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','S'], ['A','S'], [False, None]],
                [['J','D'], ['J','D'], ['Q','D'], ['J','D'], ['3','D'], [True, 'J']],
                [['5','S'], ['5','C'], ['5','D'], ['5','H'], [False, None]],
                [['3','H'], ['3','H'], ['Q','H'], ['2','H'], ['A','H'], [False, None]],
                [['10','H'], ['10','C'], ['5','D'], ['10','D'], ['5','C'], [True, '10']],
                [['10','C'], ['K','H'], ['Q','S'], ['K','D'], ['3','H'], ['6','C'], [False, None]],
                [['4','D'], ['4','C'], ['4','H'], ['K','S'], ['K','D'], ['K','H'], [True, 'K']],
                [['A','D'], ['2','D'], ['2','C'], ['A','C'], ['A','H'], [True, 'A']],
                [['A','D'], ['2','D'], ['2','C'], ['4','D'], ['2','S'], ['A','H'], [True, '2']],
                [['4','S'], ['2','D'], ['2','C'], ['4','D'], ['Q','S'], ['Q','H'], [False, None]],
                [['4','S'], ['8','C'], ['8','D'], ['4','C'], ['4','D'], ['8','S'], ['10','H'], [True, '8']],
                [['J','S'], ['J','C'], ['J','D'], ['4','C'], ['10','D'], ['10','S'], ['10','H'], [True, 'J']])
        
        for i in range(len(data)):
            check_cards = []
            names = []
            for j in range(len(data[i])-1):
                check_cards.append(Card(data[i][j][0], data[i][j][1]))
            for index in range(0, len(check_cards)):
                card = check_cards[index]
                names.append(card.name)
            num, high1 = Player.check_three_of_kind(names)
            self.assertEqual(num, data[i][-1][0], "→ Data " + str(i))
            self.assertEqual(high1, data[i][-1][1], "→ Data " + str(i))
    
    def test_check_pairs(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','S'], ['A','S'], [0, None, None]],
                [['J','D'], ['J','D'], ['Q','D'], ['J','D'], ['3','D'], [0, None, None]],
                [['5','S'], ['5','C'], ['5','D'], ['5','H'], [0, None, None]],
                [['3','H'], ['3','H'], ['Q','H'], ['2','H'], ['A','H'], [1, '3', None]],
                [['10','H'], ['10','C'], ['5','D'], ['10','D'], ['5','C'], [1, '5', None]],
                [['10','C'], ['K','H'], ['Q','S'], ['K','D'], ['3','H'], ['6','C'], [1, 'K', None]],
                [['4','D'], ['4','C'], ['3','H'], ['K','S'], ['K','D'], [2, 'K', '4']],
                [['A','D'], ['2','D'], ['2','C'], ['4','D'], ['A','H'], [2, 'A', '2']],
                [['A','D'], ['2','D'], ['2','C'], ['4','D'], ['A','S'], ['A','H'], [1, '2', None]],
                [['4','S'], ['2','D'], ['2','C'], ['4','D'], ['Q','S'], ['Q','H'], [3, 'Q', '4']],
                [['4','S'], ['8','C'], ['8','D'], ['4','C'], ['4','D'], ['10','S'], ['10','H'], [2, '10', '8']])
        
        for i in range(len(data)):
            check_cards = []
            names = []
            for j in range(len(data[i])-1):
                check_cards.append(Card(data[i][j][0], data[i][j][1]))
            for index in range(0, len(check_cards)):
                card = check_cards[index]
                names.append(card.name)
            num, high1, high2 = Player.check_pairs(names)
            self.assertEqual(num, data[i][-1][0], "→ Data " + str(i))
            self.assertEqual(high1, data[i][-1][1], "→ Data " + str(i))
            self.assertEqual(high2, data[i][-1][2], "→ Data " + str(i))
    
    def test_get_hightest_card(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','S'], ['A','S'], 'A'],
                [['10','D'], ['J','D'], ['Q','D'], ['2','D'], ['3','D'], 'Q'],
                [['5','S'], ['5','C'], ['5','D'], ['5','H'], '5'],
                [['6','H'], ['3','H'], ['Q','H'], ['2','H'], ['A','H'], 'A'],
                [['10','C'], ['J','H'], ['Q','S'], ['K','D'], ['3','H'], ['6','C'], 'K'],
                [['9','D'], ['4','C'], ['3','H'], ['2','D'], ['8','D'], '9'],
                [['10','D'], ['2','D'], ['3','D'], ['4','D'], ['7','D'], '10'],
                [['10','H'], ['J','C'], ['5','D'], ['10','D'], ['5','C'], 'J'])
        
        for i in range(len(data)):
            check_cards = []
            names = []
            for j in range(len(data[i])-1):
                check_cards.append(Card(data[i][j][0], data[i][j][1]))
            for index in range(0, len(check_cards)):
                card = check_cards[index]
                names.append(card.name)
            self.assertEqual(Player.get_hightest_card(names), data[i][-1], "→ Data " + str(i))
    
    def test_check_hand(self):
        
        data = ([['10','S'], ['J','S'], ['Q','S'], ['K','C'], ['A','S'], ['Straight', 'A', None]],
                [['J','D'], ['J','D'], ['Q','D'], ['J','H'], ['3','D'], ['Three of Kind', 'J', None]],
                [['Q','D'], ['2','D'], ['5','D'], ['4','D'], ['K','H'], ['7','D'], ['Flush', 'Q', None]],
                [['10','S'], ['J','S'], ['Q','S'], ['K','S'], ['A','S'], ['Royal Flush', None, None]],
                [['3','H'], ['3','S'], ['Q','H'], ['2','H'], ['A','H'], ['One Pair', '3', None]],
                [['10','H'], ['10','C'], ['5','D'], ['10','D'], ['5','C'], ['Full House', '10', '5']],
                [['10','C'], ['4','H'], ['Q','S'], ['K','D'], ['3','H'], ['6','C'], ['Trash', 'K', None]],
                [['4','D'], ['4','C'], ['3','H'], ['K','S'], ['K','D'], ['Two Pairs', 'K', '4']],
                [['A','D'], ['A','S'], ['A','C'], ['4','D'], ['A','H'], ['Four of Kind', 'A', None]],
                [['A','D'], ['10','H'], ['Q','H'], ['J','H'], ['K','H'], ['9','H'], ['Straight Flush', 'K', None]],
                [['4','S'], ['2','D'], ['2','C'], ['4','D'], ['Q','S'], ['Q','H'], ['Two Pairs', 'Q', '4']],
                [['4','S'], ['8','C'], ['8','D'], ['4','C'], ['4','D'], ['10','S'], ['10','H'], ["Full House", '4', '10']])
        
        for i in range(len(data)):
            player_cards = []
            community_cards = []
            for a in range(0, 2):
                player_cards.append(Card(data[i][a][0], data[i][a][1]))
            for b in range(2, len(data[i])-1):
                community_cards.append(Card(data[i][b][0], data[i][b][1]))
                
            player = Player("Test", 20, 0, 5000)
            player.take_card(player_cards)
            
            community_table = CommunityTable()
            community_table.set_cards(community_cards)
            community_table.show_card(len(community_cards))
            
            result = player.check_hand(community_table)
            self.assertEqual(result[0], data[i][-1][0], "→ Data " + str(i))
            self.assertEqual(result[1], data[i][-1][1], "→ Data " + str(i))
            self.assertEqual(result[2], data[i][-1][2], "→ Data " + str(i))
     
    # def test_to_bet(self):
    #     pass
    
    # def test_to_check(self):
    #     pass
    
    # def test_to_fold(self):
    #     pass
    
    # def test_to_call(self):
    #     pass
    
    # def test_to_all_in(self):
    #     pass
    
    # def test_to_raise(self):
    #     pass
    