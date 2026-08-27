#!/usr/bin/env python3

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["xiaohei", "shanxin", "xiaobai", "gege", "nezha", "wuxian"]
    activities = ["walk", "eat", "sleep", "attack", "climb", "defend", "heal"]
    while True:
        name = random.choice(players)
        action = random.choice(activities)
        yield (name, action)


def consume_event(
    records: list
) -> typing.Generator[tuple[str, str], None, None]:
    while records:
        out = random.choice(records)
        records.remove(out)
        yield out


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for index in range(1000):
        event = next(generator)
        print(f"Event {index}: Player {event[0]} did action {event[1]}")

    generator = gen_event()
    records = []
    for index in range(10):
        records.append(next(generator))
    print(f"Built list of {len(records)} events: {records}")

    new_records = consume_event(records)
    for out in new_records:
        print(f"Got event from list: {out}")
        print(f"Remains in list: {records}")


if __name__ == "__main__":
    main()
