#!/usr/bin/env python3


if __name__ == '__main__':
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directry")
    print("Text import now = THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire import dark_spell_record

    print(f"{dark_spell_record('Fantasy', 'Bats, frogs and eyeball')}")
