from ex0.factory import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
        factory1: CreatureFactory,
        factory2: CreatureFactory
) -> None:
    creature_1 = factory1.create_base()
    creature_2 = factory2.create_base()
    print(creature_1.describe())
    print(" vs.")
    print(creature_2.describe())
    print(" fight!")
    print(creature_1.attack())
    print(creature_2.attack())


def main() -> None:
    print("Testing factory")
    flame = FlameFactory()
    test_factory(flame)
    print()

    print("Testing factory")
    aqua = AquaFactory()
    test_factory(aqua)
    print()

    print("Testing battle")
    factory1 = FlameFactory()
    factory2 = AquaFactory()
    test_battle(factory1, factory2)


if __name__ == "__main__":
    main()
