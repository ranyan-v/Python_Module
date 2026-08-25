#!/usr/bin/env python3

import sys


# Build inventory
def parse(input: str) -> tuple[str, str] | None:
    position = 0
    item = ""
    value = ""
    if position < len(input):
        while position < len(input) and input[position] != ":":
            item += input[position]
            position += 1

        if position == len(input):
            print(f"Error - invalid parameter '{item}'")
            return None
        else:
            position += 1

        while position < len(input) and input[position] != ":":
            value += input[position]
            position += 1

        if position != len(input):
            print(f"Error - invalid parameter '{item}'")
            return None
        else:
            return (item, value)
    else:
        return None


def validate(input: tuple) -> tuple[str, int] | None:
    item = input[0]
    value = input[1]
    if item == "" or value == "":
        return None
    try:
        int_value = int(value)
    except ValueError:
        print(
            f"Quantity error for '{item}': "
            f"invalid literal for int() with base 10: '{value}'"
        )
        return None
    return (item, int_value)


def build_inventory() -> dict:
    inventory: dict[str, int] = {}
    i = 1
    while i < len(sys.argv):
        temp = parse(sys.argv[i])
        if temp is None:
            pass
        else:
            validated = (validate(temp))

        if validated is None:
            pass
        else:
            if validated[0] not in inventory.keys():
                inventory[validated[0]] = validated[1]
            else:
                print(f"Redundant item '{validated[0]}' - discarding")

        i += 1

    return inventory


# Analyze inventory
def analysis(inventory: dict) -> None:
    if not inventory:
        return

    item_list = list(inventory.keys())
    value_list = list(inventory.values())

    print(f"Item list: {item_list}")
    sum_value = sum(value_list)
    print(f"Total quantity of the {len(item_list)} items: {sum_value}")

    i = 0
    while i < len(item_list):
        percentage = round((value_list[i]/sum_value) * 100, 1)
        print(f"Item {item_list[i]} represents {percentage}%")
        i += 1

    # max
    i = 1
    max_value = value_list[0]
    max_loc = 0
    while i < len(value_list):
        if max_value < value_list[i]:
            max_value = value_list[i]
            max_loc = i
        i += 1
    print(
        f"Item most abundant: {item_list[max_loc]} "
        f"with quantity {value_list[max_loc]}"
    )

    # min
    i = 1
    min_value = value_list[0]
    min_loc = 0
    while i < len(value_list):
        if min_value > value_list[i]:
            min_value = value_list[i]
            min_loc = i
        i += 1
    print(
        f"Item least abundant: {item_list[min_loc]} "
        f"with quantity {value_list[min_loc]}"
    )


# Add new item
def add_item(inventory: dict) -> None:
    inventory.update({
        "magic_item": 1
    })
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = build_inventory()
    print(f"Got inventory: {inventory}")
    analysis(inventory)
    add_item(inventory)


if __name__ == "__main__":
    main()
