from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, name: str) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self, name: str) -> str:
        pass

    @abstractmethod
    def revert(self, name: str) -> str:
        pass
