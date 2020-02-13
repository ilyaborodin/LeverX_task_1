from abc import ABC, abstractmethod


class ArgsParser(ABC):
    """Класс служит для чтения аргументов с терминала"""
    @abstractmethod
    def _set_args(self) -> None:
        pass

    @abstractmethod
    def get_args(self) -> tuple:
        pass
