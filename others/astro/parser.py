from AsteroidAnalyzer import AsteroidAnalyzer
from result_ui import ResultUI

def parse_inputs():
    print("  Asteroid Collision Detector \n")
    name = input("Please provide the name of the asteroid : ").strip()

    if name == "":
        name = "Unknown"
    TYPES = {
        "1": ("C-type (carbonaceous)", 1380),
        "2": ("S-type (siliceous/stony)", 2710),
        "3": ("M-type (metallic)", 5320),
    }

    while True:
        print("\nThe type of the asteroid:")
        print("  1 = C-type (carbonaceous, very common)")
        print("  2 = S-type (siliceous/stony)")
        print("  3 = M-type (metallic, mostly iron/nickel)")
        choice = input("Choose type (1 / 2 / 3): ").strip()
        if choice in TYPES:
            type_name, density = TYPES[choice]
            print(f"Got it: {type_name} — density {density} kg/m3")
            break
        print("Error! Please enter 1, 2, or 3.")

    while True:
        try:
            distance = float(input("Please enter the distance (in AU): "))
            if distance < 0:
                print("Invalid ! Please try again")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        try:
            speed = float(input("Please enter the speed (in km/s): "))
            if speed < 0:
                print("Invalid ! Please try again")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        try:
            diameter = float(input("Please enter the diameter (in km): "))
            if diameter <= 0:
                print("Invalid ! Please try again")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")


    info = {
        "name":     name,
        "type":     type_name,
        "dist":  distance,
        "density":  density,
        "vel":  speed,
        "diam":  diameter,
    }
    return info

def main():
    data = parse_inputs()

    asteroid = AsteroidAnalyzer(data)
    result = asteroid.analyze_asteroid()
    result_ui = ResultUI()
    result_ui.show_result(result)

if __name__ == "__main__":
    main()
