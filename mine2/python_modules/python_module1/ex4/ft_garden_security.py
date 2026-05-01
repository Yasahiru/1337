class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print("\nInvalid operation attempted:", end=" ")
            print(f"height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print("\nInvalid operation attempted:", end=" ")
            print(f"age {new_age}y.o [REJECTED]")
            print("Security: Negative Age rejected\n")
        else:
            self.__age = new_age

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        print(f"Plant created: {self.name}")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 20, 10)
    plant.get_info()
    plant.set_height(25)
    print(f"Height updated: {plant.get_height()}cm [OK]")
    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days [OK]")
    plant.set_height(25)
    plant.set_age(-5)
    print(f"Current plant: {plant.name}", end=" ")
    print(f"({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
