def check_temperature(temp_str: int) -> int:
    print(f"Testing temperature: {temp_str}")
    try:
        tmp: int = int(temp_str)
        if (tmp > 40):
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)\n")
        if (tmp < 0):
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {tmp}°C is perfect for plants!\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature(25)
    check_temperature("abc")
    check_temperature(100)
    check_temperature(-50)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
