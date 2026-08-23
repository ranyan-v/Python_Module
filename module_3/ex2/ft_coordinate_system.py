#!/usr/bin/env python3
import math


def parse(input_data: str) -> list | None:
    coordinates_str = []
    current = ""
    location = 0
    while location < len(input_data):
        while location < len(input_data) and input_data[location] != ",":
            current += input_data[location]
            location += 1
        coordinates_str.append(current)
        current = ""
        location += 1
    if len(coordinates_str) != 3:
        print("Invalid syntax")
        return None
    else:
        return (coordinates_str)


def validate(input_data: str) -> tuple | None:
    coordinates_str = parse(input_data)
    if coordinates_str is None:
        return None
    i = 0
    coordinates_float = []
    while i < len(coordinates_str):
        try:
            value = float(coordinates_str[i])
            i += 1
            coordinates_float.append(value)
        except ValueError as error:
            print(f"Error on parameter '{coordinates_str[i]}':{error}")
            return None
    return tuple(coordinates_float)


def get_player_pos(position: str) -> tuple:
    print(f"Get a {position} set of coordinates")
    result = None
    while result is None:
        result = validate(
            input("Enter new coordinates as floats in format 'x,y,z':")
        )
    return result


def distance(position_1: tuple, position_2: tuple) -> float:
    x1 = position_1[0]
    y1 = position_1[1]
    z1 = position_1[2]
    x2 = position_2[0]
    y2 = position_2[1]
    z2 = position_2[2]

    x = (x2 - x1) * (x2 - x1)
    y = (y2 - y1) * (y2 - y1)
    z = (z2 - z1) * (z2 - z1)

    distance = math.sqrt(x + y + z)
    return round(distance, 4)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    position_1 = get_player_pos("first")
    print(f"Got a first tuple: {position_1}")
    print(
        f"It includes: X={position_1[0]}, "
        f"Y={position_1[1]}, "
        f"Z={position_1[2]}"
    )
    print(f"Distance to center: {distance((0,0,0), position_1)}")
    print()
    position_2 = get_player_pos("second")
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{distance(position_1, position_2)}"
    )


if __name__ == "__main__":
    main()
