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
    def attack(self) -> None:
        print('Flameling uses Ember!')


class Pyrodon(Creature):
    def attack(self) -> None:
        print('Pyrodon uses Flamethrower!')


class Aquabub(Creature):
    def attack(self) -> None:
        print('Aquabub uses Water Gun!')


class Torragon(Creature):
    def attack(self) -> None:
        print('Torragon uses Hydro Pump!')


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> None:
        pass

    @abstractmethod
    def create_evolved(self) -> None:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> None:
        pass

    def create_evolved(self) -> None:
        pass


class AquaFactory(CreatureFactory):
    def create_base(self) -> None:
        pass

    def create_evolved(self) -> None:
        pass


if __name__ == '__main__':
    print('Testing Factory')
