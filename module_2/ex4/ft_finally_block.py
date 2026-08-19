#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if not plant_name[0].isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    try:
        print("Testing valid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        error_type = type(error).__name__
        print(f"Caught {error_type}: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print()

    try:
        print("Testing invalid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as error:
        error_type = type(error).__name__
        print(f"Caught {error_type}: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print()


def main() -> None:
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
