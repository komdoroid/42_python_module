#!/usr/bin/env python3

import sys


def output_ancient_text(target_file: str) -> None:
    print('=== Cyber Archives Recovery ===')
    print(f"Accessing file '{target_file}'")
    f = open(target_file, 'r')
    try:
        print('---\n')
        print(f'{f.read()}')
        print('---')
    finally:
        f.close()
        print(f"File '{target_file}' closed.")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage {sys.argv[0]} <file>')
    else:
        target_file = sys.argv[1]
        try:
            output_ancient_text(target_file)
        except FileNotFoundError as e:
            print(f"Error opening file '{target_file}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{target_file}': {e}")
        except OSError as e:
            print(f"Error opening file '{target_file}': {e}")
