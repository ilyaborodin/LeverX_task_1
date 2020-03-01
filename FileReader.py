import json
from abc import ABC, abstractmethod


class FileReaderABC(ABC):
    """Класс служит для чтения данных из файлов"""
    @abstractmethod
    def load_file(self, path):
        pass


class FileReader(FileReaderABC):
    def load_file(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as file:
                json_text = json.load(file)
        except FileNotFoundError:
            raise Exception("Не найден файл по указаному пути: {0}".format(path))
        except json.decoder.JSONDecodeError:
            raise Exception("Неверный формат json")
        return json_text
