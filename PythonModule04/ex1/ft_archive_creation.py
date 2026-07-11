#!/usr/bin/env python3

import sys


def output_ancient_text(target_file: str) -> str:
    f = open(target_file, 'r')
    try:
        content: str = f.read()
    finally:
        f.close()
    return content


def add_ancient_text(content: str) -> str:
    lines = content.splitlines()
    new_content = "\n".join([line + '#' for line in lines])
    return new_content


def transform_data_procedure(target_file: str) -> str:
    print('=== Cyber Archives Recovery ===')
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


def main() -> None:
    if len(sys.argv) != 2:
        print(f'Usage {sys.argv[0]} <file>')
    else:
        target_file = sys.argv[1]
        try:
            new_content = transform_data_procedure(target_file)
            new_file_name = input('Enter new file name (or empty): ')
        except FileNotFoundError as e:
            print(f"Error opening file '{target_file}': {e}")
            return
        except PermissionError as e:
            print(f"Error opening file '{target_file}': {e}")
            return
        except OSError as e:
            print(f"Error opening file '{target_file}': {e}")
            return

        if not new_file_name:
            print('Not saving data.')
        else:
            print(f"Saving data to '{new_file_name}'")
            try:
                f = open(new_file_name, 'w')
                try:
                    f.write(new_content)
                    print(f"Data saved in file '{new_file_name}'")
                finally:
                    f.close()
            except PermissionError as e:
                print(f"Error opening file '{new_file_name}': {e}")
                return
            except OSError as e:
                print(f"Error unexpected error: {e}")
                return


if __name__ == '__main__':
    main()
