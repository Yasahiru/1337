class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        self.height += cm

    def add_days(self, days: int) -> None:
        self.age += days

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth() -> None:
    rose: Plant = Plant("Rose", 25, 30)
    oak: Plant = Plant("Oak", 200, 365)
    sunflower: Plant = Plant("Sunflower", 80, 45)

    plants: list[Plant] = [rose, oak, sunflower]
    for i in range(3):
        plant: Plant = plants[i]
        old_height: int = plant.height
        print("=== Day 1 ===")
        plant.get_info()
        plant.grow(7)
        plant.add_days(7)
        print("=== Day 7 ===")
        plant.get_info()
        print(f"Growth this week: +{plant.height - old_height}cm\n")


if __name__ == "__main__":
    ft_plant_growth()
