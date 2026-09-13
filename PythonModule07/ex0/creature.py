#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    name: str
    type: str

    @abstractmethod
    def attack(self) -> None:
        pass

    def describe(self) -> None:
        print(f'{self.name} is a {self.type} type Creature')


class Flameling(Creature):
    def __init__(self) -> None:
        self.name = 'Flameling'
        self.type = 'Fire'

    def attack(self) -> None:
        print('Flameling uses Ember!')


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = 'Pyrodon'
        self.type = 'Fire/Flying'

    def attack(self) -> None:
        print('Pyrodon uses Flamethrower!')


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name = 'Aquabub'
        self.type = 'Water'

    def attack(self) -> None:
        print('Aquabub uses Water Gun!')


class Torragon(Creature):
    def __init__(self) -> None:
        self.name = 'Torragon'
        self.type = 'Water'

    def attack(self) -> None:
        print('Torragon uses Hydro Pump!')


if __name__ == '__main__':
    c = Flameling()
    c.attack()
    print(c.type)
