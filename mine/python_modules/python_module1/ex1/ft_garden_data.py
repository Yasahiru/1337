class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    plants = [p1, p2, p3]
    for i in range(3):
        plant = plants[i]
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    ft_garden_data()
