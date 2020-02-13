from abc import ABC, abstractmethod


class FileReader(ABC):
    """Класс служит для чтения данных из файлов"""
    @abstractmethod
    def load_json_file(self, path: str):
        pass
