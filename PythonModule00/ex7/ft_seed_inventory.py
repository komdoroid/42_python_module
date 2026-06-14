def ft_seed_inventory(
        seed_type: str,
        quantity: int,
        unit: str) -> None:
    print(f">>> ft_seed_inventory(\"{seed_type}\", {quantity}, \"{unit}\")")

    capitalized_type: str = seed_type.capitalize()

    if unit == 'packets':
        print(f"{capitalized_type} seeds: {quantity} packets available")
    elif unit == 'grams':
        print(f"{capitalized_type} seeds: {quantity} grams total")
    elif unit == 'area':
        print(f"{capitalized_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
