class PlantError(Exception):
    pass


def water_plants(plant_list: list[str]) -> None:
    try:
        for plant in plant_list:
            if plant is None:
                raise PlantError()
            else:
                print(f"watering {plant}")
    except PlantError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_normal_watering() -> None:
    print("Opening watering system")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")


def test_error_watering() -> None:
    print("Testing with error...")
    water_plants(["tomato", None])


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    test_normal_watering()
    test_error_watering()
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
