#!/usr/bin/env python3

import sys
from typing import IO


def output_ancient_text(target_file: str) -> str:
    f = open(target_file, 'r')
    content: str = f.read()
    return content


def add_ancient_text(content: str) -> str:
    lines = content.splitlines()
    new_content = "\n".join([line + '#' for line in lines])
    return new_content


def transform_data_procedure(target_file: str) -> str:
    print('=== Cyber Archives Recovery ===')
    print('---\n')
    print(f"Accessing file '{target_file}'")
    print('---')
    content = output_ancient_text(target_file)
    print(content)
    print(f"File '{target_file}' closed.\n")

    print('Transform data:')
    print('---\n')
    new_content = add_ancient_text(content)
    print(new_content)
    print('---')
    return new_content


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage {sys.argv[0]} <file>')
    else:
        target_file = sys.argv[1]
        try:
            new_content = transform_data_procedure(target_file)
            new_file_name = input('Enter new file name (or empty): ')
            if not new_file_name:
                print('Not saving data.')
            else:
                print(f"Saving data to '{new_file_name}'")
                print(f"Data saved in file '{new_file_name}'")
                f = open(new_file_name, 'w')
                f.write(new_content)
        except FileNotFoundError as e:
            print(f"Error opening file '{target_file}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{target_file}': {e}")
        finally:
            f.close()
