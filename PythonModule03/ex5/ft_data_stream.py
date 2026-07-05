#! /usr/bin/python3

from typing import Generator
import random


player_list = ['alice', 'bob', 'charlie', 'dylan']
action_list = ['move', 'run', 'swim', 'climb',
               'grab', 'release', 'eat', 'sleep']


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        next_player = random.choice(player_list)
        next_action = random.choice(action_list)
        yield (next_player, next_action)


def consume_event(
        tuple_list: list[tuple[str, str]]
        ) -> Generator[tuple, None, None]:
    while True:
        random_index = random.randrange(len(tuple_list))
        removed_item = tuple_list.pop(random_index)
        yield removed_item


if __name__ == '__main__':
    print('=== Game Data Stream Processor ===')

    ge = gen_event()
    for i in range(1000):
        next_player, next_action = next(ge)
        print(f'Event {i}: Player {next_player} did action {next_action}')

    tuple_list: list[tuple[str, str]] = list()
    loop_count = 10
    for i in range(loop_count):
        tuple_list.append(next(ge))
    print(f'Built list of {loop_count} events: {tuple_list}')

    ce = consume_event(tuple_list)
    for i in range(loop_count):
        print(f'Got event from list: {next(ce)}')
        print(f'Remains in list: {tuple_list}')
