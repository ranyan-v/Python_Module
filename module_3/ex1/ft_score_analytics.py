#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    i = 1
    scores = []
    while i < len(sys.argv):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i = i + 1

    if len(scores) == 0:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        print(
            f"Scores processed: {scores}\n"
            f"Total players: {len(scores)}\n"
            f"Total score: {sum(scores)}\n"
            f"Average score: {sum(scores) / len(scores)}\n"
            f"High score: {max(scores)}\n"
            f"Low score: {min(scores)}\n"
            f"Score range: {max(scores) - min(scores)}"
        )


if __name__ == "__main__":
    main()
