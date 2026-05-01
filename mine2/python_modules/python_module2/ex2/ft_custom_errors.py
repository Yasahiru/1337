class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant_error(plant: str, age: int) -> None:
    if (age > 6):
        raise PlantError(f"Caught PlantError: The {plant} plant is wilting!")


def water_error(water_level: int) -> None:
    if (water_level < 5):
        raise WaterError("Caught WaterError: Not enough water in the tank!")


def raise_plant_error() -> None:
    try:
        plant_error("tomato", 9)
    except PlantError as e:
        print(e)


def raise_water_error() -> None:
    try:
        water_error(3)
    except WaterError as e:
        print(e)


def raise_plant_garden_error() -> None:
    try:
        plant_error("tomato", 9)
    except PlantError as e:
        print(e)


def rais_water_garden_error() -> None:
    try:
        water_error(3)
    except GardenError as e:
        print(e)


def rais_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    raise_plant_error()
    print()
    print("Testing WaterError...")
    raise_water_error()
    print()
    print("Testing catching all garden errors...")
    raise_plant_garden_error()
    rais_water_garden_error()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    rais_errors()
