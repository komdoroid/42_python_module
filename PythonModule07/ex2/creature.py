#!/usr/bin/env python3

from abc import ABC, abstractmethod
from .capability  import HealCapability, TransformCapability


class Creature(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def attack() -> None:
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


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = 'Sproutling'
        self.type = 'Grass'

    def attack(self) -> None:
        print(f'{self.name} uses Vine Whip!')

    def heal(self, target: str = 'itself') -> None:
        print(f'{self.name} heals {target} for a small amount')


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self.name = 'Bloomelle'
        self.type = 'Grass/Fairy'

    def attack(self) -> None:
        print(f'{self.name} uses Petal Dance!')

    def heal(self, target: str = 'itself') -> None:
        print(f'{self.name} heals {target} for a large amount')


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        self.name = 'Shiftling'
        self.type = 'Normal'
        self.is_transformed = False

    def attack(self) -> None:
        if self.is_transformed:
            print(f'{self.name} performs a boosted strike!')
        else:
            print(f'{self.name} attacks normally.')

    def transform(self) -> None:
        self.is_transformed = True
        print(f'{self.name} shifts into a sharper form!')

    def revert(self) -> None:
        self.is_transformed = False
        print(f'{self.name} returns to normal.')

class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        self.name = 'Morphagon'
        self.type = 'Normal/Dragon'
        self.is_transformed = False

    def attack(self) -> None:
        if self.is_transformed:
            print(f'{self.name} unleashes a devastating morph strike!')
        else:
            print(f'{self.name} attacks normally.')

    def transform(self) -> None:
        self.is_transformed = True
        print(f'{self.name} morphs into a dragonic battle form!')

    def revert(self) -> None:
        self.is_transformed = False
        print(f'{self.name} stabilizes its form.')


if __name__ == '__main__':
    c = Flameling()
    c.attack()
    print(c.type)
