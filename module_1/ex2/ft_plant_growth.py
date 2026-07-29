#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def aged(self) -> None:
        self.age += 1


def main() -> None:
    rose = Plant("Rose", 25.0, 30, 0.8)
    ini_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        rose.grow()
        rose.aged()

        print(f"=== Day {day} ===")
        rose.show()

    print(f"Growth this week: {round(rose.height - ini_height, 1)}cm")


if __name__ == "__main__":
    main()
