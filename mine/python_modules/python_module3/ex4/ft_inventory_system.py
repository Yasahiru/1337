import sys


def percent(number: int, total: int) -> float:
    return round(((number * 100) / total), 1)


def ft_inventory_system() -> None:
    try:
        inventory: dict = dict()
        total_items: int = 0
        item_types: set = set()

        for arg in sys.argv:
            if arg != sys.argv[0]:
                argument = arg.split(":")
                inventory[argument[0]] = int(argument[1])
                item_types.add(argument[0])
                total_items += int(argument[1])

        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {len(item_types)}\n")
        print("=== Current Inventory ===")

        total_items: int = round(total_items, 2)
        most_abundant: int = 0
        less_abundant: int = 0
        most_abundant_item: str = ""
        less_abundant_item: str = ""
        for key, value in inventory.items():
            print(f"{key}: {value} units "
                  f"({percent(int(value), total_items)}%)")
            if (value > most_abundant):
                most_abundant = value
                most_abundant_item = key
        less_abundant = most_abundant
        for key, value in inventory.items():
            if (value < less_abundant):
                less_abundant = value
                less_abundant_item = key
        print("\n=== Inventory Statistics ===")
        unity = "units" if most_abundant > 1 else "unit"
        print(f"Most abundant: {most_abundant_item} ({most_abundant} {unity})")
        unity = "units" if less_abundant > 1 else "unit"
        print(f"Least abundant: {less_abundant_item} "
              f"({less_abundant} {unity})\n")

        moderate_items: dict = dict()
        scarce_items: dict = dict()
        for key, value in inventory.items():
            if (value > 4 and value < 9):
                moderate_items[key] = value
            if (value < 5):
                scarce_items[key] = value
        print("=== Item Categories ===")
        print(f"Moderate: {moderate_items}")
        print(f"Scarce: {scarce_items}\n")

        restock_items: list[str] = []
        print("=== Management Suggestions ===")
        for key, value in scarce_items.items():
            if (value <= 1):
                restock_items.append(key)
        print(f"Restock needed: {restock_items}\n")

        dict_keys: list[str] = []
        dict_values: list[str] = []
        for key in inventory.keys():
            dict_keys.append(key)
        for key in inventory.values():
            dict_values.append(key)
        print("=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {dict_keys}")
        print(f"Dictionary Values: {dict_values}")

        exist: bool = False
        for item in dict_keys:
            if (item == "sword"):
                exist = True
        print(f"Sample lookup - 'sword' in inventory: {exist}")

    except Exception:
        print("Invalid arguments")


def main() -> None:
    if (len(sys.argv) < 2):
        print("No Arguments")
    else:
        print("=== Inventory System Analysis ===")
        ft_inventory_system()


if __name__ == "__main__":
    main()
