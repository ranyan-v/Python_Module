#!usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
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

# Getter
    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

# Setter
    def set_height(self, height):
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def show(self):
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


def main():
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
