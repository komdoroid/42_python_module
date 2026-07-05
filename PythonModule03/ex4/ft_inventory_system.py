#! /usr/bin/env python3

import sys


def validate_args(argv: list[str], inventory: dict[str, int]) -> None:
    for bef_split in argv[1:]:
        try:
            name_quant_list = bef_split.split(':')
            if name_quant_list[0] in inventory:
                raise TypeError(f"Redundant item '{name_quant_list[0]}'"
                                f" - discarding")
            if len(name_quant_list) != 2:
                raise TypeError(f"Error - invalid parameter "
                                f"'{name_quant_list[0]}'")
            item_name = name_quant_list[0]
            item_quant = int(name_quant_list[1])
            inventory[item_name] = item_quant
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(f"Quantity error for '{name_quant_list[0]}': {e}")


def get_quantity(key: str) -> int:
    return inventory[key]


if __name__ == '__main__':
    inventory: dict[str, int] = {}
    print('=== Inventory System Analysis ===')

    validate_args(sys.argv, inventory)
    print(f'Got inventory: {inventory}')

    key_list = list(inventory.keys())
    print(f"Item list: {key_list}")

    value_list = list(inventory.values())
    print(f'Total quantity of the {len(value_list)} items: {sum(value_list)}')

    for key in inventory.keys():
        print(f'Item {key} reresents '
              f'{round(inventory[key] / sum(value_list) * 100, 1)}%')

    min_item = min(inventory, key=get_quantity)
    max_item = max(inventory, key=get_quantity)
    print(f'Item most abundant: '
          f'{max_item} with quantity {inventory[max_item]}')
    print(f'Item least abundant: '
          f'{min_item} with quantity {inventory[min_item]}')

    inventory.update({'magic_item': 1})
    print(f'Updated inventory: {inventory}')
