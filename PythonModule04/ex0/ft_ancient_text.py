#!/usr/bin/env python3

import sys
from typing import IO


def output_ancient_text(target_file: str) -> IO[str]:
    f = open(target_file, 'r')
    print('---\n')
    print(f'{f.read()}')
    print('---')
    return f


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage {sys.argv[0]} <file>')
    else:
        target_file = sys.argv[1]
        try:
            print('=== Cyber Archives Recovery ===')
            print(f"Accessing file '{target_file}'")
            f = output_ancient_text(target_file)
            print(f"File '{target_file}' closed.")
        except FileNotFoundError as e:
            print(f"Error opening file '{target_file}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{target_file}': {e}")
        except OSError as e:
            print(f"Error opening file '{target_file}': {e}")
        finally:
            f.close()
