class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sun: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sun = sun


class GardenManager():
    plants: list[Plant] = []
    tank: int = 2

    @classmethod
    def add_plant(cls: "GardenManager", obj: Plant) -> None:
        try:
            if (obj.name == ""):
                raise PlantError(
                    "Error adding plant: Plant "
                    "name cannot be empty!\n"
                )
            cls.plants.append(obj)
            print(f"Added {obj.name} successfully")
        except PlantError as e:
            print(e)

    @classmethod
    def water_plants(cls: "GardenManager") -> None:
        print("Opening watering system")
        try:
            for plant in cls.plants:
                plant.water_level += 1
                cls.tank -= 1
                print(f"Watering {plant.name} - success")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)\n")

    @classmethod
    def check_plants_health(cls: "GardenManager"):
        try:
            for plant in cls.plants:

                """ Handling Water Level Error """
                if (plant.water_level < 1):
                    raise WaterError(
                        f"Error checking {plant.name}: water level "
                        f"{plant.water_level} is too low (min 1)\n"
                    )
                if (plant.water_level > 10):
                    raise WaterError(
                        f"Error checking {plant.name}: water level "
                        f"{plant.water_level} is too high (max 10)\n"
                    )

                """ Handling Sun Error """
                if (plant.sun < 2):
                    raise SunError(
                        f"Error checking {plant.name}: sun level "
                        f"{plant.sun} is too low (min 2)\n"
                    )
                if (plant.sun > 12):
                    raise SunError(
                        f"Error checking {plant.name}: sun level "
                        f"{plant.sun} is too high (max 12)\n"
                    )
                print(
                    f"{plant.name}: healthy (water: {plant.water_level},"
                    f" sun: {plant.sun})"
                    )
        except WaterError as e:
            print(e)
        except SunError as e:
            print(e)

    @classmethod
    def error_recovery(cls: "GardenManager"):
        try:
            if (cls.tank < 1):
                raise GardenError(
                    "Caught GardenError: Not enough water in tank"
                )
        except GardenError as e:
            print(e)
        finally:
            cls.tank += 10
            print("System recovered and continuing...\n")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    gardenManager = GardenManager()
    gardenManager.tank = 4

    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 14, 6)
    empty = Plant("", 5, 8)

    print("Adding plants to garden...")
    gardenManager.add_plant(tomato)
    gardenManager.add_plant(lettuce)
    gardenManager.add_plant(empty)

    print("Watering plants...")
    gardenManager.water_plants()

    print("Checking plant health...")
    gardenManager.check_plants_health()

    print("Testing error recovery...")
    gardenManager.error_recovery()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
