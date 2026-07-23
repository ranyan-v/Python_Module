#!/usr/bin/env python3

class Plant:
    # ---------- Constructor ----------
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name

        # Validate initial value
        if height < 0:
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            self._age = 0
        else:
            self._age = age

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
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


def main() -> None:
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()

    print()
    rose.set_height(25)
    rose.set_age(30)

    print()
    rose.set_height(-1)
    rose.set_age(-2)

    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
