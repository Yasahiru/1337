def garden_operations(val: int) -> None:
    try:
        if (val == "missing.txt"):
            open(val, "r")
        if (val == "missing"):
            int(val)
        if (val == "dict"):
            dict = {"test": "test"}
            print(dict['missing_plant'])
        if (val == "import"):
            from numpy import somethingstrange
            somethingstrange
        new_val: int = int(val)
        if (new_val == 0):
            new_val /= 0
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()\n")
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero\n")
    except FileNotFoundError:
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    except KeyError as e:
        print("Testing KeyError...")
        print(f"Caught KeyError: {e}\n")
    except Exception:
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    garden_operations("missing")
    garden_operations(0)
    garden_operations("missing.txt")
    garden_operations("dict")
    garden_operations("import")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
