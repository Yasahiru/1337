# classified_data.txt
# security_protocols.txt


def ft_vault_security() -> None:
    try:
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")

        print("SECURE EXTRACTION:")
        with open("classified_data.txt", "r") as f:
            print(f"{f.read()}\n")

        print("SECURE PRESERVATION:")
        with open("security_protocols.txt", "r") as f:
            print(f"{f.read()}")

    except Exception as e:
        print(e)
    finally:
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    ft_vault_security()


if __name__ == "__main__":
    main()
