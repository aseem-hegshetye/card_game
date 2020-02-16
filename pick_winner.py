class PickWinner:
    """ pick winner from cards provided in form of tuples"""

    def __init__(self, cards_list):
        self.cards_list = cards_list
        self.cards_int = []

    def convert_face_cards_to_numbers(self):
        """
            convert face cards like king, joker etc to number so that its easy to process
            keep the order of face cards intact. A = 14, K=13, Q=12, J=11
            keep the original format in self.face_cards intact to display to users
        """
        face_card_conversion = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}
        cards_int = []
        for card in self.cards_list:
            if isinstance(card[1], int):
                cards_int.append(card)
            else:
                cards_int.append((card[0],face_card_conversion[card[1]]))
        self.cards_int = cards_int

    def pick_winner(self):
        """
            pick a winner. use normal cards precedence A,K,Q,J,10,9.. so on
            if 1st player played (spades,K) then only (spades,A) can beat this card. (diamonds,A) wont work
            1st player sets the suit for the round.
        """
        self.convert_face_cards_to_numbers()
        main_suit = self.cards_int[0][0]  # suit that dominates this round
        winner_index = 0  # by default 1st player wins until we find a bigger card in same suit
        winner_card_value = self.cards_int[0][1]
        for index, card in enumerate(self.cards_int[1:]):
            if main_suit == card[0]:
                if winner_card_value < card[1]:
                    winner_index = index+1
                    winner_card_value = card[1]

        return winner_index

