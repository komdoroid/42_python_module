#!/usr/bin/env python3

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = '') -> None:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform() -> None:
        pass

    def revert() -> None:
        pass
