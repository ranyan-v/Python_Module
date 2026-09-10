#!/usr/bin/env python3


import typing
import abc


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank: int = 0


    @abstractmethod
    def validate(self, data: typing.Any) -> bool:


    @abstractmethod
    def ingest(self, data: typing.Any) -> None:


    
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
            ):
                return True
            else:
                return False
        else:
            return False


    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data) and isinstance(data, dict):
            item = (self.rank, str(data))
            self.storage.append(item)
            self.rank += 1
        elif self.validate(data) and isinstance(data, list):
            for obj in data:
                item = (self.rank, str(obj))
                self.storage.append(item)
                self.rank += 1
        else:
            raise ValueError("Got exception: Improper log data")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(
        f"Trying to validate input '42': {numeric.validate(42)}"
    )
    print(
        f"Trying to validate input 'Hello': {numeric.validate("Hello")}"
    )
    print(f"Test invalid ingestion of string 'foo' without prior validation: ")
    try:
        print(f"{numeric.ingest("foo")}")
    except ValueError as error:
        print(error)
    print(f"Processing data: {numeric.ingest([1, 2, 3, 4, 5])}")
    i = 0
    print("Extracting 3 values...")
    for i in range 3:
        print(f"Numeric value {i}: {numeric.output()}")
        i += 1
    


if "__name__" == "__main__":
    main()
