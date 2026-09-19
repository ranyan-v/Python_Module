print(
    "=== Kaboom 1 ===\n"
    "Access to alchemy/grimoire/dark_spellbook.py directly\n"
    "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION"
)
try:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    dark_spell_record("Black", "sunflower")
except ImportError as error:
    print(f"ImportError: {error}")
