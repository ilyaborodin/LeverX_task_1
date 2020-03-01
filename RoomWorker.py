from abc import ABC, abstractmethod


class RoomWorkerABC(ABC):
    """Класс служит для работы со списками"""
    @abstractmethod
    def merge_lists_of_students_and_rooms(self, students, rooms):
        pass


class RoomWorker(RoomWorkerABC):
    def merge_lists_of_students_and_rooms(self, students, rooms):
        for room in rooms:
            room["students"] = []
        for student in students:
            room_of_student = student["room"]
            rooms[room_of_student]["students"].append(student)
        return rooms
