#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    argument = len(sys.argv)
    if argument == 1:
        print("No arguments provided!")
        print("Total arguments: 1")
    else:
        print(f"Arguments received: {argument - 1}")
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i = i + 1
        print(f"Total arguments: {argument}")


if __name__ == "__main__":
    main()
