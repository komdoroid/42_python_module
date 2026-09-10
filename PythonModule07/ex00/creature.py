#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def attack() -> None:
        pass

    def describe() -> None:
        pass


class Flameling(Creature):
    def __init__(self) -> None:
        self.type = 'Fire'

    def attack(self) -> None:
        print('Flameling uses Ember!')


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.type = 'Fire/Flying'

    def attack(self) -> None:
        print('Pyrodon uses Flamethrower!')


class Aquabub(Creature):
    def __init__(self) -> None:
        self.type = 'Water'

    def attack(self) -> None:
        print('Aquabub uses Water Gun!')


class Torragon(Creature):
    def __init__(self) -> None:
        self.type = 'Water'

    def attack(self) -> None:
        print('Torragon uses Hydro Pump!')


if __name__ == '__main__':
    c = Flameling()
    c.attack()
    print(c.type)
