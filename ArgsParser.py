import argparse
import os
from abc import ABC, abstractmethod


class ArgsParserABC(ABC):
    """Класс служит для чтения аргументов с терминала"""
    @abstractmethod
    def _set_args(self) -> None:
        pass

    @abstractmethod
    def get_args(self) -> tuple:
        pass


class ArgsParser(ArgsParserABC):
    def __init__(self):
        self.args = None
        self._set_args()

    def _set_args(self) -> None:
        parser = argparse.ArgumentParser(description='Command-line utility.')
        parser.add_argument('path_to_students', type=argparse.FileType('r'), help='Path to students file')
        parser.add_argument('path_to_rooms', type=argparse.FileType('r'), help='Path to rooms file')
        parser.add_argument('format', choices=['json', 'xml'], help='Output format')
        self.args = parser.parse_args()

    def get_args(self) -> tuple:
        return self.args.path_to_students, self.args.path_to_rooms, self.args.format
