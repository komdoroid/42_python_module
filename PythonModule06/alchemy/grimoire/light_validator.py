def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingredients: list[str] = light_spell_allowed_ingredients()
    for ingred in allowed_ingredients:
        if ingred in ingredients:
            return "VALID"
    return "INVALID"
