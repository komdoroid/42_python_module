#! /usr/bin/env python3

import sys


def validate_args(argv: list[str]) -> None:
    for bef_split in argv[1:]:
        try:
            name_quant_list = bef_split.split(':')
            if name_quant_list[0] in inventory:
                raise ValueError(f"Redundant item '{name_quant_list[0]}' - discarding")
            if len(name_quant_list) != 2:
                raise ValueError(f"Error - invalid parameter '{name_quant_list[0]}'")
            item_name = name_quant_list[0]
            item_quant = int(name_quant_list[1])
            inventry.update(item_name:item_quant)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(f"Quantity error for '{name_quant_list[0]}'")


if __name__ == '__main__':
    print('=== Inventory System Analysis ===')
    validate_args(sys.argv)
