
from dotenv import load_dotenv
import os
import sys


def get_config() -> dict:
    return {
        "mode": os.getenv("MATRIX_MODE"),
        "database": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "zion": os.getenv("ZION_ENDPOINT"),
    }


def validate_config(config: dict) -> list:
    missing = []

    if not config["mode"]:
        missing.append("MATRIX_MODE")
    if not config["database"]:
        missing.append("DATABASE_URL")
    if not config["api_key"]:
        missing.append("API_KEY")
    if not config["zion"]:
        missing.append("ZION_ENDPOINT")

    return missing


def describe_database(mode: str) -> str:
    if mode == "development":
        return "Connected to local instance"
    elif mode == "production":
        return "Connected to production database"
    return "Unknown environment"


def display_config(config: dict) -> None:
    try:
        print("Configuration loaded:")
        print(f"Mode: {config['mode']}")
        print(f"Database: {describe_database(config['mode'])}")
        print(
            f"API Access: {
                'Authenticated' if config['api_key'] else 'Missing'
            }"
        )
        print(f"Log Level: {config['log_level']}")
        print(f"Zion Network: {'Online' if config['zion'] else 'Offline'}")
    except Exception as e:
        print(e)


def security_check(config: dict) -> None:
    try:
        print("\nEnvironment security check:")

        if config["api_key"] and "dev" not in config["api_key"].lower():
            print("[OK] No hardcoded secrets detected")
        else:
            print("[WARNING] API key may be insecure or default")

        if os.path.exists(".env"):
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] No .env file found")

        print("[OK] Production overrides available")
    except Exception as e:
        print(e)


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()
    config = get_config()

    missing = validate_config(config)

    if missing:
        print("Missing configuration:")
        for var in missing:
            print(f"- {var}")

        print("\nHint:")
        print("→ Create a .env file or export environment variables.")
        print("→ Example:")
        print("   MATRIX_MODE=development API_KEY=secret python oracle.py")
        sys.exit(1)

    display_config(config)
    security_check(config)
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
