def validate_ingredients(ingredients: str) -> str:
    _ingredients: list = ingredients.split(" ")
    valid_ingredients: list[str] = ["fire", "water", "earth", "air"]
    for ing in _ingredients:
        if ing not in valid_ingredients:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
