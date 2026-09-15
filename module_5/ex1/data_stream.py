#!/usr/bin/env python3


import typing
import abc


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        # check int
        if isinstance(data, int):
            return True
        # check float
        elif isinstance(data, float):
            return True
        # check list[int | float]
        elif isinstance(data, list):
            if all(isinstance(element, int) or isinstance(element, float)
                    for element in data):
                return True
            else:
                return False
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data) and isinstance(data, int):
            item = (self.rank, str(data))
            self.storage.append(item)
            self.rank += 1
        elif self.validate(data) and isinstance(data, float):
            item = (self.rank, str(data))
            self.storage.append(item)
            self.rank += 1
        elif self.validate(data) and isinstance(data, list):
            for obj in data:
                item = (self.rank, str(obj))
                self.storage.append(item)
                self.rank += 1
        else:
            raise ValueError("Got exception: Improper numeric data")


class TextProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            if all(isinstance(element, str) for element in data):
                return True
            else:
                return False
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) and isinstance(data, str):
            item = (self.rank, data)
            self.storage.append(item)
            self.rank += 1
        elif self.validate(data) and isinstance(data, list):
            for obj in data:
                item = (self.rank, obj)
                self.storage.append(item)
                self.rank += 1
        else:
            raise ValueError("Got exception: Improper text data")


class LogProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        # check dict[str, str]
        if isinstance(data, dict):
            if (
                all(isinstance(element, str) for element in data.keys())
                and all(isinstance(element, str) for element in data.values())
            ):
                return True
            else:
                return False
        # check list[dict[str, str]]
        elif isinstance(data, list):
            if all(
                isinstance(element, dict)
                and all(isinstance(key, str) for key in element.keys())
                and all(isinstance(value, str) for value in element.values())
                for element in data
            ):
                return True
            else:
                return False
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data) and isinstance(data, dict):
            item = (self.rank, ": ".join(data.values()))
            self.storage.append(item)
            self.rank += 1
        elif self.validate(data) and isinstance(data, list):
            for obj in data:
                item = (self.rank, ": ".join(obj.values()))
                self.storage.append(item)
                self.rank += 1
        else:
            raise ValueError("Got exception: Improper log data")


class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.statistics: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)
        self.statistics[proc] = 0

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processed = False
            for processor in self.processors:
                if processor.validate(item):
                    processed = True
                    old_len = len(processor.storage)
                    processor.ingest(item)
                    new_len = len(processor.storage)
                    self.statistics[processor] += new_len - old_len
                    break
            if not processed:
                print(
                    f"DataStream error "
                    f"- Can't process element in stream: {stream}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        for key in self.statistics:
            processed = self.statistics[key]
            remaining = len(key.storage)

            if isinstance(key, NumericProcessor):
                print(
                    f"Numeric Processor: "
                    f"total {processed} items processed, ", end=""
                    f"remaining {remaining} on processor\n"
                )

            elif isinstance(key, TextProcessor):
                print(
                    f"Text Processor: "
                    f"total {processed} items processed, ", end=""
                    f"remaining {remaining} on processor\n"
                )

            elif isinstance(key, LogProcessor):
                print(
                    f"Log Processor: "
                    f"total {processed} items processed, ", end=""
                    f"remaining {remaining} on processor\n"
                )
            else:
                print("No processor found, no data")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    data_stream: list[typing.Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print("\nRegistering Numeric Processor\n")
    numeric = NumericProcessor()
    print(f"Send first batch of data on stream: {data_stream}")
    stream.register_processor(numeric)
    stream.process_stream(data_stream)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(data_stream)
    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    # numeric
    for i in range(3):
        numeric.output()[1]
    # text
    for i in range(2):
        text.output()[1]
    # log
    for i in range(1):
        log.output()[1]

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
