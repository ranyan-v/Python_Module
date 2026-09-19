from abc import ABC, abstractmethod


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
