from abc import ABC, abstractmethod
from .creature import Creature, Sproutling, Bloomelle, Shiftling, Morphagon


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


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        sproutling = Sproutling("Sproutling", "Grass")
        return sproutling

    def create_evolved(self) -> Bloomelle:
        bloomelle = Bloomelle("Bloomelle", "Grass/Fairy")
        return bloomelle


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        shiftling = Shiftling("Shiftling", "Normal")
        return shiftling

    def create_evolved(self) -> Morphagon:
        morphagon = Morphagon("Morphagon", "Normal/Dragon")
        return morphagon
