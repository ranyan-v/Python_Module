#!/usr/bin/env python3

class Plant:
    # ---------- Nested class ----------
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow_call(self) -> None:
            self._grow_calls += 1

        def add_age_call(self) -> None:
            self._age_calls += 1

        def add_show_call(self) -> None:
            self._show_calls += 1

        def show_statistics(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    # ---------- Constructor ----------
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name

        if height < 0:
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            self._age = 0
        else:
            self._age = age

        self._statistics = Plant.Statistics()

    # ---------- Alternative constructors ----------
    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    # ---------- Utility methods ----------
    @staticmethod
    def older_than_one_year(age: int) -> bool:
        return age > 365

    # ---------- Getters ----------
    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    # ---------- Setters ----------
    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    # ---------- Behaviors ----------
    def show(self) -> None:
        self._statistics.add_show_call()
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._statistics.add_grow_call()
        self._height += 8

    def age(self) -> None:
        self._statistics.add_age_call()
        self._age += 1

    # ---------- Statistics ----------
    def show_statistics(self) -> None:
        print(f"[statistics for {self._name}]")
        self._statistics.show_statistics()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._is_blooming:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def show_statistics(self) -> None:
        super().show_statistics()
        print(f" {self._shade_calls} shade")


class Seed(Flower):
    def __init__(
        self, name: str,
        height: float,
        age: int,
        color: str,
        seed_number: int
    ) -> None:
        super().__init__(name, height, age, color)
        self._seed_number = seed_number

    def show(self) -> None:
        super().show()
        if self._is_blooming:
            print(f" Seeds: {self._seed_number}")
        else:
            print(" Seeds: 0")

    def grow(self) -> None:
        super().grow()
        self._height += 22

    def age(self) -> None:
        super().age()
        self._age += 19


def main() -> None:
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42)
    anonymous_plant = Plant.anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.older_than_one_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.older_than_one_year(400)}")
    print()
    print("=== Flower")
    rose.show()
    rose.show_statistics()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    rose.show_statistics()
    print()
    print("=== Tree")
    oak.show()
    oak.show_statistics()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show_statistics()
    print()
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    sunflower.show_statistics()
    print()
    print("=== Anonymous")
    anonymous_plant.show()
    anonymous_plant.show_statistics()


if __name__ == "__main__":
    main()
