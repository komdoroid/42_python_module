#! /usr/bin/python3

import sys


def check_arguments(argv: list[str]) -> None:
    arg_num = len(argv)

    _, *args = argv
    if arg_num == 1:
        print('No arguments provided!')
    else:
        print(f'Arguments received: {len(args)}')
        for i in range(0, len(args)):
            print(f'Argument {i + 1}: {args[i]}')
    print(f'Total arguments: {arg_num}')
    pass


if __name__ == '__main__':
    print('=== Command Quest ===')
    print(f'Program name: {sys.argv[0]}')
    check_arguments(sys.argv)
