""" distribute cards. let everyone play. pick winner"""
import random


class DistributeCards:
    def __init__(self):
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.face_cards = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]

    def all_cards_creation(self):
        """ generates all possible 52 combinations (club,10),(diamond,'A')"""
        all_cards = []
        for face_card in self.face_cards:
            for suit in self.suits:
                all_cards.append((suit, face_card))
        return all_cards

    def distribute(self, number_of_players, no_cards_per_player):
        """distribute cards amongst player. no repetition allowed"""
        cards_per_player = []  # [[player1_cards],[p2_cards]] -- p1_cards = [(clubs,A),(hearts,2)..]
        all_cards = self.all_cards_creation()
        len_all_cards = len(all_cards)
        for player in range(number_of_players):
            player_cards = []
            for card_index in range(no_cards_per_player):
                rand = random.randrange(0, len_all_cards)
                player_cards.append(all_cards[rand])
                del all_cards[rand]
                len_all_cards -= 1
            cards_per_player.append(player_cards)
        return cards_per_player
