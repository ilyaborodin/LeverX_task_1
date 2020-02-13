from abc import ABC, abstractmethod


class FileReaderABC(ABC):
    """Класс служит для чтения данных из файлов"""
    @abstractmethod
    def load_json_file(self, path: str):
        pass
