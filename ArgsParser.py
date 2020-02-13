from abc import ABC, abstractmethod


class ArgsParser(ABC):
    """Класс служит для чтения аругментов с терминала"""
    @abstractmethod
    def _set_args(self) -> None:
        pass

    @abstractmethod
    def get_args(self) -> tuple:
        pass
