#!/usr/bin/env python3

import random


all_achievements = [
    'Crafting Genius',
    'World Savior',
    'Master Explorer',
    'Collector Supreme',
    'Untouchable',
    'Boss Slayer',
    'Strategist',
    'Speed Runner',
    'Survivor',
    'Treasure Hunter',
    'Unstoppable',
    'Hidden Path Finder',
    'First Steps',
    'Sharp Mind',
    'Monster tamer',
    'Shadow Walker',
    'Legendary Chef',
    'Rich Merchant',
    'Night Owl',
    'Lucky Star',
    'Dragon Slayer',
    'Absolute Defense',
    'Fisherman',
    'God Speed',
    'Lone Wolf',
    'Beginner Luck'
]


class Player():
    def __init__(self, player_name: str, achievements: set) -> None:
        self.player_name = player_name
        self.achievements = achievements

    def show_achiev(self) -> None:
        print(f'Player {self.player_name}: {{', end='')
        print(', '.join([f"'{achiev}'" for achiev in self.achievements]),
              end='')
        print('}')


def gen_player_achievements(achiev_num: int) -> set:
    assign_achievements = random.choices(all_achievements, k=achiev_num)
    return set(assign_achievements)
    pass


if __name__ == '__main__':
    players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    player_instances = []

    for player in players:
        p = Player(player, gen_player_achievements(random.randint(8, 11)))
        player_instances.append(p)

    print('=== Achievement Tracker System ===\n')
    for p in player_instances:
        p.show_achiev()
    print('All distinct achievements: {{', end='')
    print(', '.join([f"'{achiev}'" for achiev in all_achievements]), end='')
    print('}\n')

    common_achiev = set(player_instances[0].achievements)
    for p in player_instances[1:]:
        tmp_achiev = p.achievements
        common_achiev = tmp_achiev.intersection(common_achiev)
    print(f"Common achievemnents: '{common_achiev}'\n")

    for i in range(len(player_instances)):
        new_list = player_instances.copy()
        new_list.remove(player_instances[i])
        original_achiev = player_instances[i].achievements
        for achiev in new_list:
            original_achiev = original_achiev.difference(achiev.achievements)
        print(f'Only Alice has: {original_achiev}')
    print()

    for p in player_instances:
        print(f'{p.player_name} is missing: '
              f'{set(all_achievements).difference(p.achievements)}')
