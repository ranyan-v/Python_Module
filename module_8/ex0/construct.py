from sys import executable, prefix, base_prefix
from os import path
from site import getsitepackages


def in_virtual_env() -> bool:
    return prefix != base_prefix


def main() -> None:
    if in_virtual_env():
        env_name = path.basename(prefix)
        installation_path = getsitepackages()[0]  # list of path
        print(
            "\nMATRIX STATUS: Welcome to the construct\n"
            f"\nCurrent Python: {executable}\n"
            f"Virtual Environment: {env_name}\n"
            f"Environment Path: {prefix}\n"
            "\nSUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n"
            "\nPackage installation path:\n"
            f"{installation_path}"
        )
    else:
        print(
            "\nMATRIX STATUS: You're still plugged in\n"
            f"\nCurrent Python: {executable}\n"
            "Virtual Environment: None detected\n"
            "\nWARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n"
            "\nTo enter the construct, run:\n"
            "python3 -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            "\nThen run this program again."
        )


if __name__ == "__main__":
    main()
