#!/usr/bin/env python3

from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


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


if __name__ == '__main__':
    ff = FlameFactory()
    flame = ff.create_base()
    flame.attack()
