from distribute_cards import DistributeCards
from pick_winner import PickWinner
import numpy


class Main:
    """
        Ask user to provide number of players, number of cards per player
    """
    no_of_players = int(input('How many players are playing ?\n'))
    no_of_cards_per_player = int(input('How many cards per player?\n'))
    score_per_player = numpy.zeros(no_of_players, numpy.int32)
    cards_per_player = DistributeCards().distribute(
        number_of_players=no_of_players,
        no_cards_per_player=no_of_cards_per_player
    )

    no_of_rounds = no_of_cards_per_player * 1  # making a new var
    while no_of_rounds > 0:
        cards_played_in_a_round = []
        print('\ncards_per_player=', cards_per_player)
        for player_index in range(no_of_players):
            card_index = int(input(f'player {player_index} pick your card index\n'))
            cards_played_in_a_round.append(cards_per_player[player_index][card_index])
            del cards_per_player[player_index][card_index]

        pick_winner_obj = PickWinner(cards_played_in_a_round)
        winner_index = pick_winner_obj.pick_winner()
        score_per_player[winner_index] += 1
        no_of_rounds -= 1
        print(f'score_per_player={score_per_player}')

    max_score_index = numpy.argmax(score_per_player)
    print(f'\n WINNER IS PLAYER {max_score_index}')


if __name__ == '__main__':
    Main()
