#!/usr/bin/env python3

def garden_operations(operation_num: int) -> None:
    if operation_num == 0:
        int("abc")
    elif operation_num == 1:
        42 / 0
    elif operation_num == 2:
        open("iamnothere.txt")
    elif operation_num == 3:
        "summer" + 42


def test_operations() -> None:
    for number in range(5):
        try:
            print(f"Testing operation {number}...")
            garden_operations(number)
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError
        ) as error:
            error_type = type(error).__name__
            print(f"Caught {error_type}: {error}")

    print("Operation completed successfully")
    print()
    print("All error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_operations()


if __name__ == "__main__":
    main()
