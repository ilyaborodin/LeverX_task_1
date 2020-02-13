from abc import ABC, abstractmethod


class DataExporterABC(ABC):
    """Класс служит для экпорта данных в xml и json"""
    @abstractmethod
    def export_to(self, path: str, format: str) -> dict:
        """Выбор формата для экспорта файлов"""
        pass

    @abstractmethod
    def _export_to_json(self, path: str) -> None:
        pass

    @abstractmethod
    def _export_to_xml(self, path: str) -> None:
        pass
