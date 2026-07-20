#!/usr/bin/env python3

import typing
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
    def inget(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        data = self.data_list.pop(0)
        now_rank = self.rank_counter
        self.rank_counter += 1
        return now_rank, data


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def inget(self, data: int | float | list[int | float]) -> None:
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

    def inget(self, data: str | list[str]) -> None:
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

    def inget(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            print(f"'{data}' without prior validation:")
            print('Got exception: Improper log data')
            return
        if isinstance(data, list):
            for item in data:
                result = ': '.join(item.values())
                self.data_list.append(result)
        else:
            self.data_list.append(str(data.values()))


class ExportPlugin(typing.Protocol):
    plugin_type: str

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def __init__(self) -> None:
        self.plugin_type = "CSV"

    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = ','.join([element for _, element in data])
        print("CSV Output:")
        print(result)


class JSONExportPlugin:
    def __init__(self) -> None:
        self.plugin_type = 'JSON'

    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = []
        for counter, element in data:
            json_element = f'"item_{counter}": "{element}"'
            result.append(json_element)
        print('{' + ', '.join(result) + '}')


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
                    processor.inget(data)
                    break
                # print(f"{self.__class__.__name__} error - "
                #       f"Can't process element in strem: {data}")

    def print_processors_stats(self) -> None:
        for processor in self.processors_list:
            remains = len(processor.data_list)
            if processor.__class__.__name__ == "NumericProcessor":
                print("Numeric Processor: ", end='')
            if processor.__class__.__name__ == "TextProcessor":
                print("Text Processor: ", end='')
            if processor.__class__.__name__ == "LogProcessor":
                print("Log Processor: ", end='')
            print(f"total items {remains + processor.rank_counter}, "
                  f"remaining {remains} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        print(f"Send {nb} processed data from each processor "
              f"to a {plugin.plugin_type} plugin:")
        for processor in self.processors_list:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    now_rank, element = processor.output()
                    data.append((now_rank, element))
                except Exception:
                    break
            plugin.process_output(data)


def output_datastream_statics(dataStream: DataStream) -> None:
    print("\n== DataStream statistics ==")
    dataStream.print_processors_stats()
    print()


data_list: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO',
          'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']]
another_data_list: list[Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR',
          'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
        ]

if __name__ == '__main__':
    numProcessor = NumericProcessor()
    textProcessor = TextProcessor()
    logProcessor = LogProcessor()
    dataStream = DataStream()
    csvPlugin = CSVExportPlugin()
    jsonPlugin = JSONExportPlugin()

    print('=== Code Nexus - Data Pipeline ===\n')

    print("Initialize Data Stream...")

    print("\n== DataStream statics ==")
    dataStream.process_stream([])

    print("\nRegistering Processors\n")
    dataStream.register_processor(numProcessor)
    dataStream.register_processor(textProcessor)
    dataStream.register_processor(logProcessor)

    print(f"Send first batch of data on strem: {data_list}")
    dataStream.process_stream(data_list)

    output_datastream_statics(dataStream)

    dataStream.output_pipeline(3, csvPlugin)

    output_datastream_statics(dataStream)

    print(f"Send another batch of data: {another_data_list}\n")
    dataStream.process_stream(another_data_list)

    dataStream.output_pipeline(5, jsonPlugin)

    output_datastream_statics(dataStream)
