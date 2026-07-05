#! /usr/bin/python3

import sys


def calculate_score(args: list[str]) -> None:
    scores = []

    for score in args:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    scores_num = len(scores)
    if scores_num == 0:
        print('No scores provided. '
              'Usage: python3 ft_score_analytics.py '
              '<score1> <score2> ...')
    else:
        print(f'Scores processed: {scores}')
        print(f'Total players: {scores_num}\n'
              f'Total score: {sum(scores)}\n'
              f'Average score: {sum(scores) / scores_num}\n'
              f'High score: {max(scores)}\n'
              f'Low score: {min(scores)}\n'
              f'Score range: {max(scores) - min(scores)}\n'
              )


if __name__ == '__main__':
    print('=== Player Score Analytics ===')
    calculate_score(sys.argv[1:])
