#!/usr/bin/env python3

from abc import ABC, abstractmethod
from .creature import Creature
from .factory import CreatureFactory
from .capability import HealCapability, TransformCapability

class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' for this normal strategy")
        creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AgressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' for this aggressive strategy")
        creature.transform()
        creature.attack()
        creature.revert()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' for this defensive strategy")
        creature.attack()
        creature.heal()

    def is_valid(self, creature: CreatureFactory) -> bool:
        return isinstance(creature, HealCapability)
