from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    # is_found = any(item in ingredient_low for item in target_list)
    for item in allowed:
        if item.lower() in ingredients_lower:
            is_valid = True
            break
    if is_valid:
        status = "VALID"
    else:
        status = "INVALID"
    return f"{ingredients} - {status}"
