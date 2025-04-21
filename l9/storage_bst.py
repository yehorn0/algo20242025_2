from typing import NoReturn, Iterator
from l9.bst_node import BSTNode, insert, update, find, inorder_traversal, tree_size, display
from l9.storage_proto import StorageProto, T


class StorageBST(StorageProto[T]):
    def __init__(self) -> None:
        self.__root: BSTNode[T] | None = None

    def insert(self, element: T) -> None | NoReturn:
        self.__root = insert(self.__root, element)
        return None

    def find(self, key: str) -> T | NoReturn:
        return find(self.__root, key)

    def update(self, element: T) -> None | NoReturn:
        return update(self.__root, element)

    @property
    def elements(self) -> list[T]:
        return inorder_traversal(self.__root)

    # ============================================================================================== #
    # ======================================== LAB 10 ============================================== #
    # ============================================================================================== #
    def __setitem__(self, key: str, value: T) -> None:
        """See usage in the main section
        If no key then insert new node,
        if key exists then update existing node

        Steps:
            - try find and update
            - if error insert new value to the tree
        """
        ...

    def __getitem__(self, key: str) -> T:
        """See usage in the main section
        If no key then raise KeyError

        Steps:
            - try find and return it
            - if error raise KeyError
        """
        ...
    # ============================================================================================== #
    # ============================================================================================== #
    # ============================================================================================== #

    def __len__(self) -> int:
        return tree_size(self.__root)

    def __iter__(self) -> Iterator[T]:
        yield from inorder_traversal(self.__root)

    def display(self) -> None:
        display(self.__root)


if __name__ == '__main__':
    from l9.entity import Entity
    entity_0 = Entity("e0", 10, 100.)
    entity_1 = Entity("e1", 11, 400.)
    entity_2 = Entity("e2", 12, 500.)
    entity_3 = Entity("e3", 13, 200.)

    storage = StorageBST[Entity]()

    storage.insert(entity_2)
    storage.insert(entity_1)
    storage.insert(entity_0)
    storage.insert(entity_3)

    print(storage.elements)

    print(storage.find("e1"), isinstance(entity_2, Entity))
    entity_2_updated = Entity("e2", 113, 2100.)
    storage.update(entity_2_updated)

    print(storage.elements)
    storage.display()

    for elem in storage:
        print(elem)
