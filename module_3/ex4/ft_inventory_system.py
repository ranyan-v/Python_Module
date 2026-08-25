#!/usr/bin/env python3

import sys


# Build inventory
def parse(input: str) -> tuple[str, str] | None:
    position = 0
    item = ""
    value = ""
    while position < len(input):
        while position < len(input) and input[position] != ":":
            item += input[position]
            position += 1

        if position == len(input):
            print("Error - invalid parameter '{item}'")
            return None
        else:
            position += 1

        while position < len(input) and input[position] != ":":
            value += input[position]
            position += 1

        if position != len(input):
            print("Error - invalid parameter '{item}'")
            return None
        else:
            return(item, value)


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
    inventory = {}
    i = 1
    while i < len(sys.argv):
        validated = (validate(parse(sys.argv[i])))
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

    print(f"Item most abundant: {} with quantity {}")
    print(f"Item least abundant: {} with quantity {}")

# Add new item
def add_item() -> dict | None:



def main() -> None:
	print("=== Inventory System Analysis ===")
    
    inventory = build_inventory()
    print(f"Got inventory: {inventory}")
    
    analysis(inventory)



if __name__ == "__main__":
	main()
