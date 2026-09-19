def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]
    for ingredient in allowed:
        ingredients_low = ingredients.lower()
        if ingredient in ingredients_low:
            return (f"{ingredients} - VALID")
    else:
        return (f"{ingredients} - INVALID")
