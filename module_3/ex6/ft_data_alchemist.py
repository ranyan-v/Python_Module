#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {players}")

    players_1 = [player.capitalize() for player in players]
    players_2 = [player for player in players if player.capitalize() == player]
    print(f"New list with all names capitalized: {players_1}")
    print(f"New list of capitalized names only: {players_2}")
    print()

    scores = {
        player: random.randint(0, 100)
        for player in players_1
    }
    print(f"Score dict: {scores}")

    total_score = sum(scores.values())
    average_score = round(total_score / len(scores.values()), 2)
    print(f"Score average is {average_score}")

    high_scores = {
        player: score
        for player, score in scores.items()
        if score > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
