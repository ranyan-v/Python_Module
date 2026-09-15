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


class ExportPlugin(typing.Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []
        for rank, value in data:
            values.append(value)

        result = ",".join(values)
        print("CSV Output:")
        print(result)


class JSONPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        temp: list[str] = []
        for rank, value in data:
            info = f'"item_{rank}": "{value}"'
            temp.append(info)

        result = "{" + ", ".join(temp) + "}"
        print("JSON Output:")
        print(result)


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
        if not self.statistics:
            print("No processor found, no data")
            return

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            pipeline: list[tuple[int, str]] = []

            for _ in range(nb):
                if len(processor.storage) == 0:
                    break
                else:
                    pipeline.append(processor.output())

            plugin.process_output(pipeline)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")
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
    print("\nRegistering Processors\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print(f"Send first batch of data on stream: {data_stream}\n")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    stream.process_stream(data_stream)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVPlugin()
    stream.output_pipeline(3, csv_plugin)
    print()

    stream.print_processors_stats()

    data_stream_2: list[typing.Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {data_stream_2}\n")
    stream.process_stream(data_stream_2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONPlugin()
    stream.output_pipeline(5, json_plugin)
    print()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
