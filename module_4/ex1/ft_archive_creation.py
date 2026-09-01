#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    # Read data
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery & Preservation ===")
        file_name = sys.argv[1]
        try:
            print(f"Accessing file '{file_name}'")
            file: typing.IO = open(file_name, "r")
            content = file.read()
            print("---\n")
            print(content)
            print("\n---")
            file.close()
            print(f"File '{file_name}' closed.\n")
        except OSError as error:
            print(f"Error opening file '{file_name}': {error}")
            return
    else:
        print(F"Usage: {sys.argv[0]} <file>")
        return

    # Transform data
    trans = ""
    if content != "":
        print("Transform data:")
        print("---\n")
        for character in content:
            if character == "\n":
                trans = trans + "#\n"
            else:
                trans = trans + character
        if content[-1] != "\n":
            trans = trans + "#"
        print(trans)
        print("\n---")

    new_file_name = input("Enter new file name (or empty):")
    if new_file_name == "":
        print("Not saving data.")
    else:
        try:
            print(f"Saving data to '{new_file_name}'")
            new_file: typing.IO = open(new_file_name, "w")
            new_file.write(trans)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'.")
        except OSError as error:
            print(f"Error opening file '{new_file_name}': {error}")


if __name__ == "__main__":
    main()
