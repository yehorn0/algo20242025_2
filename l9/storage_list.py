from typing import NoReturn
from l9.entity import Entity
from l9.storage_proto import StorageProto, T



class StorageList(StorageProto[T]):
    def __init__(self) -> None:
        self.__elements: list[T] = []

    def insert(self, element: T) -> None | NoReturn:
        # Complexity: Time: O(n); Space: O(1)
        # consider using binary search
        current_pos: int = 0

        while current_pos < len(self.__elements):
            if self.__elements[current_pos].key > element.key:
                break
            current_pos += 1

        self.__elements.insert(current_pos, element)
        return None

    def find(self, key: str) -> T | NoReturn:
        # Complexity: Time: O(n); Space: O(1)
        for element in self.__elements:
            if element.key == key:
                return element

        raise KeyError(f'Key {key} not found')

    def update(self, element: T) -> None | NoReturn:
        # Complexity: Time: O(n); Space: O(1)
        target: T = self.find(element.key)
        target.update(element)
        return None

    @property
    def elements(self) -> list[T]:
        return self.__elements


if __name__ == '__main__':
    entity_0 = Entity("e0", 10, 100.)
    entity_1 = Entity("e1", 11, 400.)
    entity_2 = Entity("e2", 12, 500.)
    entity_3 = Entity("e3", 13, 200.)

    storage = StorageList[Entity]()

    storage.insert(entity_0)
    storage.insert(entity_1)
    storage.insert(entity_2)
    storage.insert(entity_3)

    print(storage.elements)

    print(storage.find("e1"), isinstance(entity_2, Entity))
    entity_2_updated = Entity("e2", 113, 2100.)
    storage.update(entity_2_updated)

    print(storage.elements)
