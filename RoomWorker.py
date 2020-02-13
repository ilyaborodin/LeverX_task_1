from abc import ABC, abstractmethod


class RoomWorkerABC(ABC):
    """Класс служит для работы со списками"""
    @abstractmethod
    def merge_lists_of_students_and_rooms(self, students: list, rooms: list) -> list:
        pass


class RoomWorker(RoomWorkerABC):
    def merge_lists_of_students_and_rooms(self, students: list, rooms: list) -> list:
        for student in students:
            room_of_student = student["room"]
            if "students" in rooms[room_of_student].keys():
                del student["room"]
                rooms[room_of_student]["students"].append(student)
            else:
                del student["room"]
                rooms[room_of_student]["students"] = [student, ]
        return rooms
