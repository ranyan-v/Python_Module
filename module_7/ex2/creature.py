from abc import ABC, abstractmethod
from .capability import HealCapability, TransformCapability


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    @abstractmethod
    def attack(self) -> str:
        pass


# 🔥 Flameling: The Fire-type
class Flameling(Creature):

    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


# 🔥+ Pyrodon: The evolved Fire-type
class Pyrodon(Creature):

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")


# 💧 Aquabub: The Water-type
class Aquabub(Creature):

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun!")


# 💧+ Torragon: The evolved Water-type
class Torragon(Creature):

    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump!")


# 🌱 Sproutling: The seedling stage
class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")

    def heal(self, name: str) -> str:
        return (f"{name} heals itself for a small amount")


# 🌸 Bloomelle: The flowering stage
class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")

    def heal(self, name: str) -> str:
        return (f"{name} itself and others for a large amount")


# 🌀 Shiftling: The transitional stage
class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.state = "normal"

    def attack(self) -> str:
        if self.state == "normal":
            return (f"{self.name} attacks normally.")
        else:
            return (f"{self.name} performs a boosted strike!")

    def transform(self, name: str) -> str:
        self.state = "transformed"
        return (f"{name} shifts into a sharper form!")

    def revert(self, name: str) -> str:
        self.state = "normal"
        return (f"{name} returns to normal.")


# 🌀+ MorphagonConcept: The final stage
class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.state = "normal"

    def attack(self) -> str:
        if self.state == "normal":
            return (f"{self.name} attacks normally.")
        else:
            return (f"{self.name} unleashes a devastating morph strike!")

    def transform(self, name: str) -> str:
        self.state = "transformed"
        return (f"{name} shifts into a  dragonic battle form!")

    def revert(self, name: str) -> str:
        self.state = "normal"
        return (f"{name} stabilizes its form.")
