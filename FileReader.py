import json
from abc import ABC, abstractmethod


class FileReaderABC(ABC):
    """Класс служит для чтения данных из файлов"""
    @abstractmethod
    def load_json_file(self, path: str):
        pass


class FileReader(FileReaderABC):
    def load_json_file(self, path: str):
        try:
            with open(path, 'r', encoding='utf-8') as file:
                json_text = json.load(file)
        except FileNotFoundError:
            print("Не найден файл по указаному пути: {0}".format(path))
            raise
        except json.decoder.JSONDecodeError:
            print("Неверный формат json")
            raise
        return json_text
