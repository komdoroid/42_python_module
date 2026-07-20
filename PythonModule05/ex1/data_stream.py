#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_list: list[str] = []
        self.rank_counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        now_rank = self.rank_counter
        self.rank_counter += 1
        return now_rank, self.data_list.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            print(f"'{data}' without prior validation:")
            print(' Got exception: Improper numeric data')
            return
        if isinstance(data, list):
            for i in range(len(data)):
                self.data_list.append(str(data[i]))
        else:
            self.data_list.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            print(f"'{data}' without prior validation:")
            print('Got exception: Improper text data')
            return
        if isinstance(data, list):
            for i in range(len(data)):
                self.data_list.append(str(data[i]))
        else:
            self.data_list.append(str(data))


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            return all(isinstance(item, dict) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            print(f"'{data}' without prior validation:")
            print('Got exception: Improper log data')
            return
        if isinstance(data, list):
            for item in data:
                result = ': '.join(item.values())
                self.data_list.append(result)
        else:
            result = ': '.join(str(v) for v in data.values())
            self.data_list.append(str(data.values()))


class DataStream():
    def __init__(self) -> None:
        self.processors_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        if not stream:
            pass
        if not self.processors_list:
            print("No processor found, no data")
        for data in stream:
            for processor in self.processors_list:
                if processor.validate(data):
                    processor.ingest(data)
                    break
            else:
                print(f"{self.__class__.__name__} error - "
                      f"Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        for processor in self.processors_list:
            remains = len(processor.data_list)
            if processor.__class__.__name__ == "NumericProcessor":
                print("Numeric Processor: ", end='')
            if processor.__class__.__name__ == "TextProcessor":
                print("Text Processor: ", end='')
            if processor.__class__.__name__ == "LogProcessor":
                print("Log Processor: ", end='')
            print(f"total {remains + processor.rank_counter} items processed, "
                  f"remaining {remains} on processor")


empty_data_list: list[str] = []
data_list: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']]


if __name__ == '__main__':
    numProcessor = NumericProcessor()
    textProcessor = TextProcessor()
    logProcessor = LogProcessor()
    dataStream = DataStream()

    print('=== Code Nexus - Data Stream ===\n')

    print("Initialize Data Stream...")
    print("== DataStream statics ==\n")

    dataStream.process_stream(empty_data_list)

    print("\nRegistering Numeric Processor\n")
    dataStream.register_processor(numProcessor)

    print(f"Send first batch of data on stream: {data_list}")
    dataStream.process_stream(data_list)
    print("== DataStream statistics ==")
    dataStream.print_processors_stats()

    print("\nRegistering other data processors")
    dataStream.register_processor(textProcessor)
    dataStream.register_processor(logProcessor)
    print("Send the same batch again")
    dataStream.process_stream(data_list)
    print("== DataStream statistics ==")
    dataStream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numProcessor.output()
    for _ in range(2):
        textProcessor.output()
    for _ in range(1):
        logProcessor.output()
    print("== DataStream statistics ==")
    dataStream.print_processors_stats()
