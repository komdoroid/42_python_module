#! /usr/bin/python3

import sys


if __name__ == '__main__':
    arg_num = len(sys.argv)
    print(f'Program name: {sys.argv[0]}')

    _, *args = sys.argv
    print(f'Arguments received: {len(args)}')
    if arg_num == 1:
        print('No arguments provided!')
    else:
        for i in range(0, len(args)):
            print(f'Argument {i}: {args[i]}')
    print(f'Total arguments: {arg_num}')
