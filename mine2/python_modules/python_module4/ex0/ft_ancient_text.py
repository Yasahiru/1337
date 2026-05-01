# ancient_fragment.txt


def ft_ancient_text() -> None:
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")
        print("RECOVERED DATA:")

        f = open("ancient_fragment.txt", "r")
        print(f.read())
        f.close()

    except FileNotFoundError as e:
        print(e)
    finally:
        print("\nData recovery complete. Storage unit disconnected.")


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    ft_ancient_text()


if __name__ == "__main__":
    main()
