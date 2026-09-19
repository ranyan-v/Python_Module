from .elements import create_air  # -> Relative import for a_4 5

from .potions import strength_potion  # -> Relative import for d_1
from .potions import healing_potion as heal

from alchemy import transmutation  # -> Absolute import for t_2
# from . import transmutation -> Relative import for t_2

# 声明哪些名字属于 public API
__all__ = [
    "create_air",
    "strength_potion",
    "heal",
    "transmutation"
]
