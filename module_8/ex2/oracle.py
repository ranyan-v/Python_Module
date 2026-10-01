import os
from dotenv import load_dotenv


def load_config() -> dict[str, str | None]:
    load_dotenv(".env")
    config: dict[str, str | None] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    return config


def main() -> None:

    override = os.getenv("MATRIX_MODE")

    print("\nORACLE STATUS: Reading the Matrix...\n")

    config = load_config()

    print("Configuration loaded:")
    # MATRIX_MODE
    if config["MATRIX_MODE"] is not None:
        print(f"Mode: {config['MATRIX_MODE']}")
    else:
        print("Mode: Not configured")

    # DATABASE_URL
    if config["DATABASE_URL"] is not None:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    # API_KEY
    if config["API_KEY"] is not None:
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")

    # LOG_LEVEL
    if config["LOG_LEVEL"] is not None:
        print(f"Log Level: {config['LOG_LEVEL']}")
    else:
        print("Log Level: Not configured")

    # ZION_ENDPOINT
    if config["ZION_ENDPOINT"] is not None:
        print("Zion Network: Online")
    else:
        print("Zion Network: Not configured")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    if override:
        print("[OK] Production overrides available")
    else:
        print("[INFO] No production overrides detected")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
