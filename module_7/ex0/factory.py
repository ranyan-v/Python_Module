from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


# 是ABC 因为要定义所有 concrete factory 必须提供的创建接口
# Every concrete factory must know
# how to create a base Creature and an evolved Creature.
class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        flameling = Flameling("Flameling", "Fire")
        return flameling

    def create_evolved(self) -> Creature:
        pyrodon = Pyrodon("Pyrodon", "Fire/Flying")
        return pyrodon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        aquabub = Aquabub("Aquabub", "Water")
        return aquabub

    def create_evolved(self) -> Creature:
        torragon = Torragon("Torragon", "Water")
        return torragon
