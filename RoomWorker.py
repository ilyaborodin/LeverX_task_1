from abc import ABC, abstractmethod


class RoomWorkerABC(ABC):
    """Класс служит для работы со списками"""
    @abstractmethod
    def merge_lists_of_students_and_rooms(self, students: list, rooms: list) -> list:
        pass
