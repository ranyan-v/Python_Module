from elements import create_fire, create_water # -> absolute import（绝对导入）
from .elements import create_air, create_earth # -> relative import（相对导入）


def healing_potion() -> str:
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"

def strength_potion() -> str:
    return f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
