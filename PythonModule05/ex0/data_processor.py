#! /usr/bin/env/ python3

import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    data_list = []
    validated = []

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass


    @abstractmethod
    def inget(self, ) -> None:
        pass


    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False


    def inget(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            print(f"'{data}' without prior validation:", end='')
            print('Got exception: Improper numeric data')
            return
        self.data_list.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data:any) -> bool:
        pass


    def inget() -> None:
        pass


class LogProcessor(DataProcessor):
    def validate(self, data: any) -> bool:
        pass


    def inget() -> None:
        pass


if __name__ == '__main__':
    numProcessor = NumericProcessor()
    textProcessor = TextProcessor()
    logProcessor = LogProcessor()
    num_data = 42
    str_data = 'Hello'
    foo_data = 'foo'

    print('=== Code Nexus - Data Processor ===\n')

    print('Testing Numeric Processor...')
    print(f" Trying to validate input '{num_data}'"
          f": {numProcessor.validate(num_data)}")
    print(f" Trying to validate input '{str_data}'"
          f": {numProcessor.validate(num_data)}")
    print(f"Test invalid ingestion of string {numProcessor.inget(foo_data)}")
