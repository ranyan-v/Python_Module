#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        file_name = sys.argv[1]
        try:
            print(f"Accessing file '{file_name}'")
            file: typing.IO = open(file_name, "r")
            content = file.read()
            print("---\n")
            print(content)
            print("\n---")
            file.close()
            print(f"File '{file_name}' closed.")
        except OSError as error:
            print(f"Error opening file '{file_name}': {error}")
            return
    else:
        print(F"Usage: {sys.argv[0]} <file>")


if __name__ == "__main__":
    main()
