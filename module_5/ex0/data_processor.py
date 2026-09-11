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
            if all(isinstance(element, int) or isinstance(element, float) for element in data):
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


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print(f"Test invalid ingestion of string 'foo' without prior validation: ")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(error)
    data_1: list[int | float] = [1, 2, 3, 4, 5]
    numeric.validate(data_1)
    numeric.ingest(data_1)
    print(f"Processing data: {data_1}")
    print("Extracting 3 values...")
    for i in range(3):
        print(f"Numeric value {i}: {numeric.output()[1]}")
    
    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    data_2: list[str] = ['Hello', 'Nexus', 'World']
    text.validate(data_2)
    text.ingest(data_2)
    print(f"Processing data: {data_2}")
    print("Extracting 1 values...")
    for i in range(1):
        print(f"Text value {i}: {text.output()[1]}")
    
    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    data_3: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'}, 
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    log.validate(data_3)
    log.ingest(data_3)
    print(f"Processing data: {data_3}")
    print("Extracting 2 values...")
    for i in range(2):
        print(f"Log value {i}: {log.output()[1]}")


if __name__ == "__main__":
    main()
