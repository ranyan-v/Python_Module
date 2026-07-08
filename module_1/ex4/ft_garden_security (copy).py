#!usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = value
        print(f"Height updated: {self._height}cm")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = value
        print(f"Age updated: {self._age} days")

    def show(self):
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


def main():
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()

    rose.height = 25
    rose.age = 30

    rose.height = -1
    rose.age = -2

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
