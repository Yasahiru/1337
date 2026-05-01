class Plant_health_error(Exception):
    pass


def check_plant_health(name: str, water_level: int, sun_hours: int) -> None:
    try:
        if (name == ""):
            raise Plant_health_error("Error: Plant name cannot be empty!\n")
        if (water_level < 1):
            raise Plant_health_error(
                f"Error: Water level {water_level} "
                f"is too low (min 1)\n"
            )
        if (water_level > 10):
            raise Plant_health_error(
                f"Error: Water level {water_level} "
                f"is too high (max 10)\n"
            )
        if (sun_hours < 2):
            raise Plant_health_error(
                f"Error: Sunlight hours "
                f"{sun_hours} is too low (min 2)\n"
            )
        if (sun_hours > 12):
            raise Plant_health_error(
                f"Error: Sunlight hours "
                f"{sun_hours} is too high (max 12)\n"
            )
        print(f"{name} is healthy!\n")
    except Plant_health_error as e:
        print(e)


def test_plant_checks() -> None:
    print("Testing good values...")
    check_plant_health("tomato", 2, 2)
    print("Testing empty plant name...")
    check_plant_health("", 13, 8)
    print("Testing bad water level...")
    check_plant_health("tomato", 0, 0)
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 8, 1)
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
