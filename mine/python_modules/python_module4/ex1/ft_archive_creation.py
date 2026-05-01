
def ft_archive_creation() -> None:
    try:
        print("Initializing new storage unit: new_discovery.txt")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")

        f: any = open("new_discovery.txt", "w")
        content: str = "[ENTRY 001] New quantum algorithm discovered\n"
        content += "[ENTRY 002] Efficiency increased by 347%\n"
        content += "[ENTRY 003] Archived by Data Archivist trainee"

        f.write(content)
        f.close()

        f: any = open("new_discovery.txt", "r")
        print(f"{f.read()}\n")

        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except FileNotFoundError as e:
        print(e)
    finally:
        f.close()


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    ft_archive_creation()


if __name__ == "__main__":
    main()
