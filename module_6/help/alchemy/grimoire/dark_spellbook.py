from alchemy.grimoire.dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)

    if "VALID" in validation and "INVALID" not in validation:
        return "Spell recorded"
    else:
        return "Spell rejected"
