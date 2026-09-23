from abc import ABC, abstractmethod
from .creature import (
    Creature, Flameling, Pyrodon, Aquabub, Torragon,
    Sproutling, Bloomelle, Shiftling, Morphagon
)


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
