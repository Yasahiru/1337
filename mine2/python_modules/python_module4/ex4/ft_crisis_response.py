# create: classified_vault.txt !!!!
# standard_archive.txt


def ft_crisis_response(file_name: str) -> None:
    try:

        with open(file_name, "r") as f:
            print(f"ROUTINE ACCESS: Attempting access to \'{file_name}\'")
            print(f"SUCCESS: Archive recovered - ``{f.read()}``")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to \'{file_name}\'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to \'{file_name}\'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception as e:
        print(f"{e}")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    ft_crisis_response("lost_archive.txt")
    ft_crisis_response("classified_vault.txt")
    ft_crisis_response("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
