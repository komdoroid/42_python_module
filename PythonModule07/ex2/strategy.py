#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import TypeGuard
from .creature import Creature
from .capability import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class TransformableCreature(Creature, TransformCapability):
    pass


class HealableCreature(Creature, HealCapability):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' "
                    f"for this normal strategy")
        creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' "
                    f"for this aggressive strategy")
        creature.transform()
        creature.attack()
        creature.revert()

    def is_valid(
            self, creature: Creature
            ) -> TypeGuard[TransformableCreature]:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                    f"Invalid Creature '{creature.name}' "
                    f"for this defensive strategy")
        creature.attack()
        creature.heal()

    def is_valid(self, creature: Creature) -> TypeGuard[HealableCreature]:
        return isinstance(creature, HealCapability)
