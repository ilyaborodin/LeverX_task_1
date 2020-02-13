import json
import dicttoxml
from abc import ABC, abstractmethod
from xml.dom.minidom import parseString


class DataExporterABC(ABC):
    """Класс служит для экпорта данных в xml и json"""
    @abstractmethod
    def export_to(self, data_to_export: list or dict, format_of_output: str) -> None:
        """Выбор формата для экспорта файлов"""
        pass

    @abstractmethod
    def _export_to_json(self, data_to_export: list or dict) -> None:
        pass

    @abstractmethod
    def _export_to_xml(self, data_to_export: list or dict) -> None:
        pass


class DataExporter(DataExporterABC):
    def export_to(self, data_to_export: list or dict, format_of_output: str) -> None:
        if format_of_output == "json":
            self._export_to_json(data_to_export)
        else:
            self._export_to_xml(data_to_export)

    def _export_to_json(self, data_to_export: list or dict) -> None:
        with open("output.json", "w", encoding="utf-8") as file:
            json_text = json.dumps(data_to_export, indent=2)
            file.writelines(json_text)

    def _export_to_xml(self, data_to_export: list or dict) -> None:
        xml = dicttoxml.dicttoxml(data_to_export)
        parsed_xml = parseString(xml)
        with open("output.xml", "w", encoding="utf-8") as file:
            file.write(parsed_xml.toprettyxml())
