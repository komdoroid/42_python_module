#! /usr/bin/env/ python3

import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_list = []
        self.rank_counter = 0

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass


    @abstractmethod
    def inget(self, ) -> None:
        pass


    def output(self) -> tuple[int, str]:
        now_rank = self.rank_counter
        self.rank_counter += 1
        return now_rank, self.data_list.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data) -> bool:
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
    def validate(self, data: any) -> bool:
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
    def validate(self, data: any) -> bool:
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


num_data = 42
str_data = 'Hello'
foo_data = 'foo'
num_data_list = [1, 2, 3, 4, 5]
str_data_list = ['Hello', 'Nexus', 'World']
dict_data_list = [{'log_level': 'NOTICE',
              'log_message': 'Connection to server'},
             {'log_level': 'ERROR',
              'log_message': 'Unauthorized access!!'}]


def output_num_processor(numProcessor: NumericProcessor) -> None:
    print(f" Trying to validate input '{num_data}'"
          f": {numProcessor.validate(num_data)}")
    print(f" Trying to validate input '{str_data}'"
          f": {numProcessor.validate(str_data)}")
    print(" Test invalid ingestion of string ", end='')
    numProcessor.inget(foo_data)
    print(f" Processing data: {num_data_list}")
    loop_count = 3
    print(f" Extracting {loop_count} values...")
    if numProcessor.validate(num_data_list):
        numProcessor.inget(num_data_list)
    for i in range(loop_count):
        rank_counter, pop_data = numProcessor.output()
        print(f" Numeric value {rank_counter}: {pop_data}")
    print()


def output_text_processor(textProcessor: TextProcessor) -> None:
    print(f" Trying to validate input '{num_data}'"
          f": {textProcessor.validate(num_data)}")
    print(f" Processing data: {str_data_list}")
    loop_count = 1
    print(f" Extracting {loop_count} values...")
    if textProcessor.validate(str_data_list):
        textProcessor.inget(str_data_list)
    for i in range(loop_count):
        rank_counter, pop_data = textProcessor.output()
        print(f" Text value {rank_counter}: {pop_data}")
    print()


def output_log_processor(logProcessor: LogProcessor) -> None:
    print(f" Trying to validate input '{str_data}'"
          f": {logProcessor.validate(str_data)}")
    print(f" Processing data: {dict_data_list}")
    loop_count = 2
    print(f" Extracting {loop_count} values...")
    if logProcessor.validate(dict_data_list):
        logProcessor.inget(dict_data_list)
    for i in range(loop_count):
        rank_counter, pop_data = logProcessor.output()
        print(f" Log {rank_counter}: {pop_data}")


if __name__ == '__main__':
    numProcessor = NumericProcessor()
    textProcessor = TextProcessor()
    logProcessor = LogProcessor()


    print('=== Code Nexus - Data Processor ===\n')

    print('Testing Numeric Processor...')
    output_num_processor(numProcessor)

    print('Testing Text Processor...')
    output_text_processor(textProcessor)

    print('Testing Log Processor...')
    output_log_processor(logProcessor)
