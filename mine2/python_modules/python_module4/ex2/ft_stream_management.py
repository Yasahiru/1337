import sys


def ft_stream_management() -> None:
    try:
        archivist_id: str = input("Input Stream active. Enter archivist ID: ")
        status_report: str = input(
                "Input Stream active. Enter status report: "
            )

        sys.stdout.write(
                        f"\n[STANDARD] Archive status from "
                        f"{archivist_id}: {status_report}\n"
                    )
        sys.stderr.write(
            "[ALERT] System diagnostic: Communication channels verified\n"
        )
        sys.stdout.write("[STANDARD] Data transmission complete\n")
    except Exception as e:
        print(e)
    finally:
        print("\nThree-channel communication test successful.")


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    ft_stream_management()


if __name__ == "__main__":
    main()
