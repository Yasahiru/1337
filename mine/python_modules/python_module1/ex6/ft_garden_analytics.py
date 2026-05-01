class Plant:

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> str:
        self.height += 1
        return f"{self.name} grew 1cm"

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"

    def get_type(self) -> str:
        return "regular"

    def get_score(self) -> int:
        return self.height


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, color: str, is_blooming: bool):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming

    def grow(self) -> str:
        self.is_blooming = True
        return super().grow()

    def get_info(self) -> str:
        state = "blooming" if self.is_blooming else "not blooming"
        return f"- {self.name}: {self.height}cm,{self.color} flowers ({state})"

    def get_type(self) -> str:
        return "flowering"

    def get_score(self) -> int:
        return self.height


class PrizeFlower(FloweringPlant):

    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        is_blooming: bool,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, color, is_blooming)
        self.prize_points = prize_points

    def get_info(self) -> str:
        state = "blooming" if self.is_blooming else "not blooming"
        return (
            f"- {self.name}: {self.height}cm, {self.color} flowers ({state}), "
            f"Prize points: {self.prize_points}"
        )

    def get_type(self) -> str:
        return "prize"

    def get_score(self) -> int:
        return self.height + self.prize_points


class Garden:
    def __init__(
        self,
        owner: str,
        plants: list[Plant],
        stats: "Garden.GardenManager",
    ) -> None:
        self.owner = owner
        self.plants = plants
        self.stats = stats

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.stats.stats.register_plant(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            print(plant.grow())
            self.stats.stats.register_growth(1)

    def generate_report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        print(self.stats.stats.get_summary())

    class GardenManager:
        total_gardens = 0

        def __init__(self) -> None:
            self.gardens: list[Garden] = []
            self.stats = Garden.GardenManager.GardenStats()

        def add_garden(self, garden: "Garden") -> None:
            self.gardens.append(garden)
            Garden.GardenManager.total_gardens += 1

        def compare_gardens(self) -> None:
            g1, g2 = self.gardens[:2]
            s1 = self.calculate_garden_score(g1)
            s2 = self.calculate_garden_score(g2)
            print(f"Garden scores - {g1.owner}: {s1}, {g2.owner}: {s2}")

        @classmethod
        def create_garden_network(cls) -> "Garden.GardenManager":
            return cls()

        @classmethod
        def get_total_gardens(cls) -> int:
            return cls.total_gardens

        @staticmethod
        def validate_plant_height(height: int) -> bool:
            return height >= 0

        @staticmethod
        def calculate_garden_score(garden: "Garden") -> int:
            score: int = 0
            for plant in garden.plants:
                score += plant.get_score()
            return score

        class GardenStats:
            def __init__(self) -> None:
                self.plants_added = 0
                self.total_growth = 0
                self.regular_count = 0
                self.flowering_count = 0
                self.prize_count = 0

            def register_plant(self, plant: Plant) -> None:
                self.plants_added += 1
                plant_type: str = plant.get_type()
                if plant_type == "prize":
                    self.prize_count += 1
                elif plant_type == "flowering":
                    self.flowering_count += 1
                else:
                    self.regular_count += 1

            def register_growth(self, amount: int) -> None:
                self.total_growth += amount

            def get_summary(self) -> str:
                return (
                    f"\nPlants added: {self.plants_added}, "
                    f"Total growth: {self.total_growth}cm\n"
                    f"Plant types: {self.regular_count} regular, "
                    f"{self.flowering_count} flowering, "
                    f"{self.prize_count} prize flowers\n"
                )


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")

    manager: Garden = Garden.GardenManager.create_garden_network()

    alice: Garden = Garden("Alice", [], manager)
    bob: Garden = Garden("Bob", [], manager)

    manager.add_garden(alice)
    manager.add_garden(bob)

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red", False))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", False, 10))

    bob.add_plant(Plant("Oak Tree", 100))

    print()
    alice.grow_all_plants()
    print()
    alice.generate_report()
    print(f"Height validation test: {manager.validate_plant_height(10)}")

    manager.compare_gardens()
    print(f"Total gardens managed: {manager.get_total_gardens()}")


if __name__ == "__main__":
    ft_garden_analytics()
