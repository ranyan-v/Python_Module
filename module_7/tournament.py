from ex2.creature import Creature
from ex2.factory import (
    CreatureFactory, FlameFactory, AquaFactory,
    HealingCreatureFactory, TransformCreatureFactory
)
from ex2.strategy import (
    BattleStrategy, NormalStrategy,
    AggressiveStrategy, DefensiveStrategy
)
from ex2.errors import BattleError


def test_battle(
        creature_1: Creature,
        strategy_1: BattleStrategy,
        creature_2: Creature,
        strategy_2: BattleStrategy
) -> None:
    print("* Battle *")
    print(creature_1.describe())
    print(" vs.")
    print(creature_2.describe())
    print(" now fight!")
    print(strategy_1.act(creature_1))
    print(strategy_2.act(creature_2))


def tournament(
    participants: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(participants)} opponents involved\n")
    player = []
    for factory, strategy in participants:
        player.append((factory.create_base(), strategy))

    i = 0
    while i < len(player):
        j = i + 1
        while j < len(player):
            creature_1, strategy_1 = player[i]
            creature_2, strategy_2 = player[j]
            try:
                test_battle(
                    creature_1, strategy_1,
                    creature_2, strategy_2
                )
                if not i == len(player) - 2:
                    print()
            except BattleError as error:
                print(f"Battle error, aborting tournament: {error}\n")
                return
            j += 1
        i += 1


def main() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    tournament([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    tournament([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ])


if __name__ == "__main__":
    main()
