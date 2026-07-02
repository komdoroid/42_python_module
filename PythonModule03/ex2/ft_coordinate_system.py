#! /usr/bin/python3

import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        try:
            user_input = input(
                    "Enter new coordinates as floats in format 'x,y,z': "
                    )
            input_list = [value for value in user_input.split(',')]
            coords = []
            if len(input_list) != 3:
                raise ValueError('Invalid syntax')
            for value in input_list:
                try:
                    coords.append(float(value))
                except ValueError:
                    raise ValueError(f"Enter on parameter '{value}': "
                          f"could not convert string to float: '{value}'")
            x, y, z = coords
            return (x, y, z)
        except ValueError as e:
            print(e)
            continue


def calc_distance(
        x1: float, x2: float,
        y1: float, y2: float,
        z1: float, z2: float
        ) -> float:
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


if __name__ == '__main__':
    print('=== Game Coordinate System ===\n')

    print('Get a first set of coordinates')
    x1, y1, z1 = get_player_pos()
    print(f'Got a first tuple: ({x1}, {y1}, {z1})')
    print(f'It includes: X={x1}, Y={y1}, Z={z1}')
    print(f'Distance to center: '
          f'{round(calc_distance(x1, 0, y1, 0, z1, 0), 4)}\n')

    print('Get a second set of coordinates')
    x2, y2, z2 = get_player_pos()
    print(f'Distance between the 2 sets of coordinates: '
          f'{round(calc_distance(x1, x2, y1, y2, z1, z2), 4)}')
