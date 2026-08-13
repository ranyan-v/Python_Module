#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


#check whether the plants' health violates the defined rule -- raise PlantError
def check_plant_health(health: int) -> None:
    if health < 0:
        raise PlantError
    else:
        return


def test_case() -> None:
    
    


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    test_case()


if __name__ == "__main__":
    main()
