class Plant:
    count: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_growth() -> None:
    rose: Plant = Plant("Rose", 25, 30)
    oak: Plant = Plant("Oak", 200, 365)
    cactus: Plant = Plant("Cactus", 5, 90)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    fern: Plant = Plant("Fern", 15, 120)

    plants: list[Plant] = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for i in range(5):
        plant: Plant = plants[i]
        plant.get_info()
    print(f"\nTotal plants created: {fern.count}")


if __name__ == "__main__":
    ft_plant_growth()
