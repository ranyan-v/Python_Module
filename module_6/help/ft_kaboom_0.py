# import alchemy.grimoire.light_validator as g1
# import alchemy.grimoire.light_spellbook as g0
import alchemy.grimoire as g0

spell_name = "Fantasy"
ingredients = "Earth, wind and fire"
print(
    "=== Kaboom 0 ===\n"
    "Using grimoire module directly\n"
    f"Testing record light spell: \
{g0.light_spell_record(spell_name, ingredients)}\
: {spell_name} ({g0.validate_ingredients(ingredients)})\n"
)
