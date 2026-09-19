from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    for ingredient in allowed:
        ingredients_low = ingredients.lower()
        if ingredient in ingredients_low:
            return (f"{ingredients} - VALID")
    else:
        return (f"{ingredients} - INVALID")
