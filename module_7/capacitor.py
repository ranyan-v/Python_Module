from ex1.factory import (
    HealingCreatureFactory,
    TransformCreatureFactory
)


def test_heal(factory: HealingCreatureFactory) -> None:
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal(base.name))

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal(evolved.name))


def test_transform(factory: TransformCreatureFactory) -> None:
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform(base.name))
    print(base.attack())
    print(base.revert(base.name))

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform(evolved.name))
    print(evolved.attack())
    print(evolved.revert(evolved.name))


def main() -> None:
    print("Testing Creature with healing capability")
    healing = HealingCreatureFactory()
    test_heal(healing)
    print()

    print("Testing Creature with transform capability")
    transform = TransformCreatureFactory()
    test_transform(transform)
    print()


if __name__ == "__main__":
    main()
