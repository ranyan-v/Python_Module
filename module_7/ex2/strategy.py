from abc import ABC, abstractmethod
from .creature import Creature
from .capability import HealCapability, TransformCapability
from .errors import BattleError


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, TransformCapability))

    def act(self, creature: Creature) -> str:
        if isinstance(creature, TransformCapability):
            result = (
                creature.transform(creature.name)
                + "\n"
                + creature.attack()
                + "\n"
                + creature.revert(creature.name)
            )
            return result
        else:
            raise BattleError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, HealCapability))

    def act(self, creature: Creature) -> str:
        if isinstance(creature, HealCapability):
            result = (
                creature.attack()
                + "\n"
                + creature.heal(creature.name)
            )
            return result
        else:
            raise BattleError(
                f"Invalid Creature '{creature.name}' for this healing strategy"
            )
