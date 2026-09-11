#!/usr/bin/env python3

from abc import ABC, abstractmethod
from .creature import Creature, Sproutling, Bloomelle, Shiftling, Morphagon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> None:
        pass

    @abstractmethod
    def create_evolved(self) -> None:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> None:
        return Flameling()

    def create_evolved(self) -> None:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> None:
        return Aquabub()

    def create_evolved(self) -> None:
        return Torragon()


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> None:
        return Sproutling()

    def create_evolved(self) -> None:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> None:
        return Shiftling()

    def create_evolved(self) -> None:
        return Morphagon()


if __name__ == '__main__':
    ff = FlameFactory()
    flame = ff.create_base()
    flame.attack()
