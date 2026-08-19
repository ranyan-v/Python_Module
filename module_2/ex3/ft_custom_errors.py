#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


# check whether the plants' health violates the defined rule -- raise
def check_plant_health(plant_name: str, health: int) -> None:
    if health < 0:
        raise PlantError(f"The {plant_name} is wilting!")


# check whether the water level violates the defined rule
def check_water_level(water_level: int) -> None:
    if water_level < 2:
        raise WaterError("Not enough water in the tank!")


def print_error(error: GardenError) -> None:
    error_type = type(error).__name__
    print(f"Caught {error_type}: {error}")


def test_case() -> None:
    try:
        print("Testing PlantError...")
        check_plant_health("tomato plant", -1)
    except PlantError as error:
        print_error(error)
        print()

    try:
        print("Testing WaterError...")
        check_water_level(0)
    except WaterError as error:
        print_error(error)
        print()

    print("Testing catching all garden errors...")
    try:
        check_plant_health("tomato plant", -1)
    except GardenError as error:
        print_error(error)

    try:
        check_water_level(0)
    except GardenError as error:
        print_error(error)

    print()
    print("All custom error types work correctly!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    test_case()


if __name__ == "__main__":
    main()
