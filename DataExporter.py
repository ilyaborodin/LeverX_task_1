import json
import dicttoxml
from abc import ABC, abstractmethod
from xml.dom.minidom import parseString


class DataExporterABC(ABC):
    """Класс служит для экпорта данных в xml и json"""
    @abstractmethod
    def export_to(self, data_to_export, format_of_output):
        """Выбор формата для экспорта файлов"""
        pass


class DataExporter(DataExporterABC):
    def export_to(self, data_to_export, format_of_output):
        if format_of_output == "json":
            JsonExporter().export(data_to_export)
        else:
            XmlExporter().export(data_to_export)


class JsonExporter:
    def export(self, data_to_export):
        with open("output.json", "w", encoding="utf-8") as file:
            json_text = json.dumps(data_to_export, indent=2)
            file.writelines(json_text)


class XmlExporter:
    def export(self, data_to_export):
        xml = dicttoxml.dicttoxml(data_to_export)
        parsed_xml = parseString(xml)
        with open("output.xml", "w", encoding="utf-8") as file:
            file.write(parsed_xml.toprettyxml())
