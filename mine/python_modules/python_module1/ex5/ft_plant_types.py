class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm", end=" ")
        print(f"{self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def provides_shadow(self) -> None:
        print(f"{self.name} provides", end=" ")
        print(f"{self.trunk_diameter} square meters of shade")

    def get_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm,", end=" ")
        print(f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self) -> None:
        print(f"{self.name} is rich in vitamin C")

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm", end=" ")
        print(f"{self.age} days, {self.harvest_season} harvest")


def ft_plant_types() -> None:
    rose: Plant = Flower("Rose", 25, 30, "red")
    sunflower: Plant = Flower("Sunflower", 25, 30, "yellow")

    oak: Plant = Tree("Oak", 500, 1825, 50)
    sakura: Plant = Tree("Sakura", 1000, 2000, 30)

    tomato: Plant = Vegetable("Tomato", 10, 14, "Summer")
    carrot: Plant = Vegetable("Carrot", 8, 10, "Winter")

    flowers: Plant = [rose, sunflower]
    trees: Plant = [oak, sakura]
    vegetables: Plant = [tomato, carrot]
    print("=== Garden Plant Types ===\n")
    for i in range(2):
        plant: Plant = flowers[i]
        plant.get_info()
        plant.bloom()
    print()
    for i in range(2):
        plant: Plant = trees[i]
        plant.get_info()
        plant.provides_shadow()
    print()
    for i in range(2):
        plant: Plant = vegetables[i]
        plant.get_info()
        plant.nutritional_value()


if __name__ == "__main__":
    ft_plant_types()
