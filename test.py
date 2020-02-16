import unittest
from distribute_cards import DistributeCards
from pick_winner import PickWinner


class MyTestCase(unittest.TestCase):
    def test_all_cards_creation(self):
        """ test if cards are created correctly"""
        all_cards = DistributeCards().all_cards_creation()
        self.assertEqual(len(all_cards), 52)

    def test_convert_face_cards_to_numbers(self):
        """test if all face cards are now int"""
        cards = [('diamonds', 'A'), ('clubs', 'K'), ('diamonds', 'Q'), ('clubs', 'J'), ('diamonds', 5)]
        cards_int = [('diamonds', 14), ('clubs', 13), ('diamonds', 12), ('clubs', 11), ('diamonds', 5)]
        pick_winner_obj = PickWinner(cards_list=cards)
        pick_winner_obj.convert_face_cards_to_numbers()
        self.assertEqual(pick_winner_obj.cards_int, cards_int)

    def test_distribute_cards(self):
        """test if cards distribution works"""
        number_of_players = 2
        no_cards_per_player = 2
        cards_per_player = DistributeCards().distribute(number_of_players, no_cards_per_player)
        self.assertEqual(len(cards_per_player), number_of_players)
        self.assertEqual(len(cards_per_player[0]), no_cards_per_player)

    def test_pick_winner(self):
        """test if winner is being picked correctly"""
        cards = [[('diamonds', 4), ('clubs', 4)],
                 [('diamonds', 4), ('clubs', 4), ('diamonds', 'A')],
                 [('hearts', 'J'), ('spades', 'J'), ('hearts', 'Q'), ('hearts', 'K'), ('spades', 2)]]
        winner = [0, 2, 3]
        for index, card in enumerate(cards):
            winner_index = PickWinner(cards_list=card).pick_winner()
            self.assertEqual(winner_index, winner[index])


if __name__ == '__main__':
    unittest.main()
