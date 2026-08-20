#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    i = 1
    score = []
    while i < len(sys.argv):
        try:
            score.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i = i + 1

    if (len(score) == 0):
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        print(
            f"Scores processed: {score}\n"
            f"Total players: {len(score)}\n"
            f"Total score: {sum(score)}\n"
            f"Average score: {sum(score) / len(score)}\n"
            f"High score: {max(score)}\n"
            f"Low score: {min(score)}\n"
            f"Score range: {max(score) - min(score)}"
        )


if __name__ == "__main__":
    main()
