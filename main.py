from ArgsParser import ArgsParser
from RoomWorker import RoomWorker
from FileReader import FileReader
from DataExporter import DataExporter


def main():
    args_parser = ArgsParser()
    path_of_students_file, path_of_rooms_file, format_of_output = args_parser.get_args()
    file_reader = FileReader()
    students = file_reader.load_json_file(path_of_students_file)
    rooms = file_reader.load_json_file(path_of_rooms_file)
    room_worker = RoomWorker()
    merged_list = room_worker.merge_lists_of_students_and_rooms(students, rooms)
    data_exporter = DataExporter()
    data_exporter.export_to(merged_list, format_of_output)


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print("Произошла ошибка: {0}\nВыход из программы".format(str(err)))
