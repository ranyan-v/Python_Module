#!/usr/bin/env python3

import random


def gen_player_achievements(achievement_pool: list) -> set:
    achievements: set[str] = set()
    achievement_count = random.randint(5, 10)

    while len(achievements) < achievement_count:
        achievements.add(random.choice(achievement_pool))

    return achievements


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    achievement_pool = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
    ]

    # generate players
    player_list = ["Alice", "Bob", "Charlie", "Dylan"]
    player_achievements = []
    i = 0
    while i < len(player_list):
        player_achievements.append(gen_player_achievements(achievement_pool))
        print(f"Player: {player_list[i]}: {player_achievements[i]}")
        i += 1
    print()

    # union
    achievements_union = set.union(*player_achievements)
    print(f"All distinct achievements: {achievements_union}\n")

    # intersection
    achievements_inter = set.intersection(*player_achievements)
    print(f"Common achievements: {achievements_inter}\n")

    # difference
    i = 0
    while i < len(player_list):
        other_achievement = (
            player_achievements[:i] + player_achievements[i + 1:]
        )
        other_uni_achievement = set.union(*other_achievement)
        uni_achievement = set.difference(
            player_achievements[i],
            other_uni_achievement
        )
        print(f"Only {player_list[i]} has: {uni_achievement}")
        i += 1
    print()

    i = 0
    while i < len(player_list):
        missing_achievement = set.difference(
            set(achievement_pool),
            player_achievements[i]
        )
        print(f"{player_list[i]} is missing: {missing_achievement}")
        i += 1


if __name__ == "__main__":
    main()
