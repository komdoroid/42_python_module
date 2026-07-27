from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    for ingred in allowed_ingredients:
        if ingred in ingredients:
            return "VALID"
    return "INVALID"
