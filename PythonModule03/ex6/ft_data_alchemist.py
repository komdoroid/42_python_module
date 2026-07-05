#! /usr/bin/env python3

import random


players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
           'Gregory', 'john', 'kevin', 'Liam']


if __name__ == '__main__':
    print(f'Initial list of players: {players}')

    all_capitalized_players = [player.capitalize() for player in players]
    print(f'New list wieh all names capitalized: {all_capitalized_players}')

    capitalized_names_only = [
            player for player in players if player[0].isupper()
            ]
    print(f'New list of capitalized names only: {capitalized_names_only}')

    score_dict = {
            player: random.randint(0, 999)
            for player in all_capitalized_players
            }
    print(f'Score dict: {score_dict}')
    score_ave = sum(score_dict.values()) / len(score_dict)
    print(f'Score average is {round(score_ave, 2)}')
    high_score = {key: value
                  for key, value in score_dict.items()
                  if value > score_ave}
    print(f'High scores: {high_score}')
