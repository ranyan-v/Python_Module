#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temperature = int(temp_str)
    return (temperature)


def test_temperature() -> None:
    test_case = ["25", "abc"]

    for value in test_case:
        try:
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}°C")
            print()
        except ValueError as v_error:
            print(f"Caught input_temperature error: {v_error}")
            print()

    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
